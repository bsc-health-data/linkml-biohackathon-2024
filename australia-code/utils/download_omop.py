import redivis
import argparse
import re

# condition occurence: condition_occurrence:6fn1
# person: person:cdwn
# concept: concept:w5gj
# Set up argument parser
parser = argparse.ArgumentParser(description="Download OMOP data and save to a specified folder.")
parser.add_argument("--output_file", help="The output file to save the data.")
parser.add_argument("--mode", choices=["full", "sample"], default="sample", help="Mode to run the query in: 'full' or 'sample'.")
parser.add_argument("--table", default="condition_occurrence:6fn1", help="The table to query from redivis dataset.")
parser.add_argument("--output_folder", default=".", help="Folder to save the output file in.")
parser.add_argument("--limit", type=int, help="Limit the number of rows to download.")
args = parser.parse_args()

if args.mode == "full":

    user = redivis.user("demo")
    dataset = user.dataset("cms_synthetic_patient_data_omop:ye2v:v2_0")

    table = args.table
    table_name = table.split(":")[0]

    if args.limit:
        query = dataset.query(f"""
            SELECT * FROM {table} LIMIT {args.limit}
        """)
    else:
        query = dataset.query(f"""
            SELECT * FROM {table}
        """)

    # Load table as a dataframe
    df = query.to_pandas_dataframe()
    
    df.to_csv(f"{args.output_folder}/omop_{table_name}.tsv", index = False, sep = '\t')

elif args.mode == "sample":

    user = redivis.user("jamesbradleysyd")
    project = user.project("omopp:scee")


    tables = ["person_subset_output:py03", "condition_occurrence_subset_output:104y", "condition_era_subset_output:w1ke", "death_subset_output:90pm", "device_exposure_subset_output:e50r","dose_era_subset_output:wjkz", "drug_era_subset_output:yhzm", "drug_exposure_subset_output:tmsg", "observation_subset_output:rzra", " observation_period_subset_output:dx7y", "player_plan_subset_output:vhq5", "procedure_occurrence_subset_output:3vz7" ]

    for table_code in tables:

        table = project.table(table_code)
        df = table.to_pandas_dataframe()
        table_name = re.match(r'^(.*?)_subset', table_code).group(1)
        df.to_csv(f"{args.output_folder}/omop_{table_name}.tsv", index=False, sep='\t')
    
