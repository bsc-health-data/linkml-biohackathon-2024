from linkml_runtime.utils.schema_as_dict import schema_as_dict
from schema_automator.generalizers.csv_data_generalizer import CsvDataGeneralizer
import yaml
import sys

profiler = CsvDataGeneralizer()
schema = profiler.convert(file=sys.argv[1], class_name=sys.argv[2], schema_name=sys.argv[3])
s = yaml.safe_dump(schema_as_dict(schema), sort_keys=False)
yaml.dump(schema_as_dict(schema), sys.stdout)





