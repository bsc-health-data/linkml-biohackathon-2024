# Cohort Meta Schema for LinkML

The purpose of this schema is to be the link for mapping all the other data models. Thus, avoiding multiple pairwise conversions.



## setup environment

```bash
python -mvenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

validate the example data files
```bash
linkml-validate --schema ../linkmlModels/metaCohortModel/metaCohortModel.yaml examples/cohort_data.yaml
linkml-validate --schema ../linkmlModels/metaCohortModel/metaCohortModel.yaml examples/cohort_data.csv --target-class Subject
```

transform
```bash
linkml-map --verbose map-data \
  --transformer-specification examples/transform.yaml \
  --schema ../linkmlModels/metaCohortModel/metaCohortModel.yaml \
  --output output/cohort_data.yaml \
  cohort_data.yaml
```
