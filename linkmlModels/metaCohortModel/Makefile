
# Directories
EXAMPLES_DIR := examples
OUTPUT_DIR := output
TRANSFORMERS := $(wildcard ./transformer*)
EXAMPLES := $(wildcard $(EXAMPLES_DIR)/cohort*)



$(OUTPUT_DIR)/cohort_data_omop_person.yaml: $(EXAMPLES) metaCohortModel.yaml $(TRANSFORMERS)
	linkml-map --verbose map-data \
      --transformer-specification transformer-common-omop-person.yaml \
      --schema metaCohortModel.yaml \
      --output output/cohort_data_omop_person.yaml \
      examples/cohort_data.yaml

$(OUTPUT_DIR)/cohort_data_omop_condition.yaml: $(EXAMPLES) metaCohortModel.yaml $(TRANSFORMERS)
	linkml-map --verbose map-data \
      --transformer-specification transformer-common-omop-condition.yaml \
      --schema metaCohortModel.yaml \
      --output output/cohort_data_omop_condition.yaml \
      examples/cohort_data.yaml

all: $(OUTPUT_DIR)/cohort_data_omop_condition.yaml $(OUTPUT_DIR)/cohort_data_omop_person.yaml
