
setup environment
```bash
python -mvenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
generate python model from linkml file
```bash
gen-python ../linkmlModels/metaCohortModel/metaCohortModel.yaml > cohort.py
```

validate the example data files
```bash
linkml-validate --schema ../linkmlModels/metaCohortModel/metaCohortModel.yaml cohort_data.yaml
linkml-validate --schema ../linkmlModels/metaCohortModel/metaCohortModel.yaml cohort_data.csv --target-class Subject
```

transform
```bash
linkml-map --verbose map-data \
  --transformer-specification ./transform.yaml \
  --schema ../linkmlModels/metaCohortModel/metaCohortModel.yaml \
  --output output/cohort_data.yaml \
  cohort_data.yaml
```
