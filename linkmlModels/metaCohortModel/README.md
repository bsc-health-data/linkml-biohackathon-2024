# Cohort Meta Schema for LinkML

The purpose of this schema is to be the link for mapping all the other data models. Thus, avoiding multiple pairwise conversions.



## setup environment

```bash
python -mvenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## validate the example data files
```bash
linkml-validate --schema metaCohortModel.yaml examples/cohort_data.yaml
linkml-validate --schema metaCohortModel.yaml examples/cohort_data.csv --target-class Subject
```

## transform
run the make file and see the output files in `output/`
```bash
make all
```

## Notes

- csv transform does not work
