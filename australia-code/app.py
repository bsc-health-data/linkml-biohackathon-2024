import streamlit as st
import numpy as np
import pandas as pd
from io import StringIO
import time
import sys
import json
import yaml
import pandas
from linkml_runtime.utils.schema_as_dict import schema_as_dict
from schema_automator.generalizers.csv_data_generalizer import CsvDataGeneralizer
from schema_builders.omop.transformer import convert_to_standard

INPUT_FILENAME = 'input.tsv'

if 'is_converting' not in st.session_state:
  st.session_state.is_converting = False
if 'is_converted' not in st.session_state:
  st.session_state.is_converted = False
if 'data' not in st.session_state:
  st.session_state.data = None

def reset():
  st.session_state.is_converted = False
  st.session_state.data = None

def convert():
  st.session_state.is_converting = True
  st.session_state.is_converted = False

def format_output_data(format, model, uploaded_file):
  df = pandas.read_csv(uploaded_file, sep='\t')
  converted_rows = df.apply(lambda row: convert_to_standard(row[['sex', 'age', 'disease']].to_dict(), model), axis=1)
  if (model == 'OMOP'):
    persons = [item['person'] for item in converted_rows]
    condition_occurences = [item['condition_occurence'] for item in converted_rows]
    data = {
      'persons': persons,
      'condition_occurences': condition_occurences
    }
  if model == 'FHIR':
    data = list(converted_rows)

  if format == 'YAML':
    return yaml.safe_dump(data, sort_keys=False)
  elif format == 'JSON':
    return json.dumps(data)
  else:
    return 'Hello world?'

def format_output_extension(format, filename='output'):
  if format == 'YAML':
    return f'{filename}.yml'
  elif format == 'JSON':
    return f'{filename}.json'
  else:
    return f'{filename}.txt'
  
def format_output_mimetype(format):
  if format == 'YAML':
    return 'application/x-yml'
  elif format == 'JSON':
    return 'application/json'
  else:
    return 'text/plain'

st.header('Data Model Conversion')
uploaded_file = st.file_uploader("Upload a file to convert", type=['tsv'])

if uploaded_file:
  # File path located at => uploaded_file._file_urls.upload_url
  # To convert to a string based IO:
  stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

  # Save to filesystem so we can reference later
  with open(INPUT_FILENAME, 'wb') as f: 
    f.write(uploaded_file.getvalue())

  st.write('File Preview:')
  with st.container(height=500):
    st.code(stringio.read(), language='tsv', line_numbers=True)

  output_model = st.selectbox('Select the model the file should conform to', ['OMOP', 'FHIR', 'Phenopackets', 'B1MG'])
  output_format = st.selectbox('Select the output file format', ['JSON', 'YAML'], on_change=reset)

st.button(
  'Convert',
  disabled=not uploaded_file or st.session_state.is_converting,
  help="Please upload a file to convert" if not uploaded_file else "",
  on_click=convert,
)
st.divider()

if st.session_state.is_converting:
  with st.spinner('Converting...'):
    st.session_state.data = format_output_data(output_format, output_model, uploaded_file)
    st.session_state.is_converting = False
    st.session_state.is_converted = True
    st.success('Conversion Completed!')

if uploaded_file and st.session_state.is_converted and st.session_state.data:
  st.download_button(
    label=f"Download {output_format}",
    data=st.session_state.data,
    file_name=format_output_extension(output_format),
    mime=format_output_mimetype(output_format),
  )
