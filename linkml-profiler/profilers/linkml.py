from linkml_runtime.utils.schema_as_dict import schema_as_dict
from schema_automator.generalizers.csv_data_generalizer import CsvDataGeneralizer
from schema_automator.generalizers.pandas_generalizer import PandasDataGeneralizer
from linkml.generators.yamlgen import YAMLGenerator
import yaml
import os

class LinkMLProfiler():
    def __init__(self, uploaded_file):
        self.profiler = CsvDataGeneralizer()

        # Save uploaded file temporarily to disk
        with open(os.path.join("tempDir", uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())

        self.file_path = os.path.join("tempDir", uploaded_file.name)
        self.class_name = 'MyClass'
        self.schema_name = 'MySchema'

    def profile(self):
        schema = self.profiler.convert(self.file_path, class_name=self.class_name, schema_name=self.schema_name)
        s = yaml.safe_dump(schema_as_dict(schema), sort_keys=False)
        return s
    