# Data Model Converter

This app converts clinical data into a standards-compliant format (eg OMOP, FHIR, Phenopackets and B1MG data models).
The app was developed as part of the 2024 Bio-Hackathon, made possible by Elixir and Australian BioCommons.

## Installation

### 1. Create and activate virtual Python environment
```sh
$ python -m venv .venv
$ source .venv/bin/activate
```

### 2. Install requirements
```sh
$ pip install -r requirements.txt
```

### 3. Run the UI application
```sh
$ streamlit run app.py

# To run without automatically opening the browser
$ streamlit run app.py --server.headless true
```

## Using the application

1. Upload a TSV file with headers `age`, `sex`, and `disease`. (`example-data/omop/omop_example_20.tsv` has been provided as an example)
2. Select the desired data model from the dropdown.
3. Select the desired format for the download.
4. Click the convert button.
5. After the conversion, click the download button to download the data.
