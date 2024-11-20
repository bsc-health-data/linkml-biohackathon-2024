import logging
import sys
import os

import yaml
from linkml_map import ObjectTransformer
from linkml_map.cli.cli import map_data
from linkml_map.session import Session
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper


# 	linkml-map --verbose map-data \
#       --transformer-specification transformer-common-omop-condition.yaml \
#       --schema metaCohortModel.yaml \
#       --output output/cohort_data_omop_condition.yaml \
#       examples/cohort_data.yaml

def map_data(
        input,
        schema,
        source_type,
        transformer_specification,
        output,
        output_format,
        **kwargs,
):
    """
    Map data from a source schema to a target schema using a transformation specification.

    Example:

        linkml-map map-data -T X-to-Y-tr.yaml -s X.yaml  X-data.yaml
    """
    logging.info(f"Transforming {input} conforming to {schema} using {transformer_specification}")
    tr = ObjectTransformer(**kwargs)
    tr.source_schemaview = SchemaView(schema)
    tr.load_transformer_specification(transformer_specification)
    with open(input) as file:
        input_obj = yaml.safe_load(file)

    tr.index(input_obj, source_type)
    tr_obj = tr.map_object(input_obj, source_type)
    if output:
        outfile = open(output, "w", encoding="utf-8")
    else:
        outfile = sys.stdout
    outfile.write(yaml_dumper.dumps(tr_obj))


if __name__ == '__main__':
    map_data('examples/cohort_data.yaml',
             'metaCohortModel.yaml',
             'CohortData',
             'transformer-common-omop-condition.yaml',
             'cohort_data_omop_condition.yaml',
             'yaml')


