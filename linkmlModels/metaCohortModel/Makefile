
output/cohort_data_omop_person.yaml: examples/cohort_data.yaml metaCohortModel.yaml transformer-common-omop-person.yaml
	linkml-map --verbose map-data \
      --transformer-specification transformer-common-omop-person.yaml \
      --schema metaCohortModel.yaml \
      --output output/cohort_data_omop_person.yaml \
      examples/cohort_data.yaml

output/cohort_data_omop_condition.yaml: examples/cohort_data.yaml metaCohortModel.yaml transformer-common-omop-person.yaml
	linkml-map --verbose map-data \
      --transformer-specification transformer-common-omop-condition.yaml \
      --schema metaCohortModel.yaml \
      --output output/cohort_data_omop_condition.yaml \
      examples/cohort_data.yaml

all: output/cohort_data_omop_condition.yaml output/cohort_data_omop_person.yaml
