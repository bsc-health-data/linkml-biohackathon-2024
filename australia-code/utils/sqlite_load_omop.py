import sqlite3
import csv
import sys
import os

"""
This script was built for OMOP v5.4 https://ohdsi.github.io/CommonDataModel/cdm54.html
Synthetic data obtained from https://redivis.com/datasets/ye2v-6skh7wdr7/tables
"""

# Usage: python3 utils/sqlite_load_omop.py
# Then you can view the sqlite database by running:
# sqlite3 omop_full.db 
# select * from person; 
# etc. etc.

tables = ["person","observation_period","condition_occurrence","drug_exposure","procedure_occurrence","device_exposure","observation","death","location","care_site","provider","cost","drug_era","dose_era","condition_era","concept","vocabulary","domain","concept_class","concept_relationship","relationship","concept_ancestor","drug_strength"]

sql_files = [
    'OMOPCDM_sqlite_5.4_ddl.sql',   
]
def execute_sql_file(conn, file_path):
    """Execute SQL commands from a file on an SQLite connection."""
    with open(file_path, 'r') as sql_file:
        sql_script = sql_file.read()
    try:
        conn.executescript(sql_script)
    except Exception as e:
        print(conn.execute, e)
        sys.exit()
    print(f"Executed {file_path}")

def load_sql_files_in_order(db_name, sql_files):
    """Load a list of SQL files in a specified order into the SQLite database."""
    conn = sqlite3.connect(db_name)

    # Enabling foreign key support if there are foreign key constraints
    conn.execute("PRAGMA foreign_keys = ON;")
    
    for file_path in sql_files:
        execute_sql_file(conn, os.path.join('models/omop', file_path))

    conn.commit()
    conn.close()
    print("All SQL files executed successfully.")

def load_tsv_to_table(db_name, tsv_file_path, table_name):
    """Load data from a TSV file into a specified table in the SQLite database."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    with open(tsv_file_path, 'r', newline='') as file:
        reader = csv.reader(file, delimiter='\t')
        headers = next(reader)  # Get column names from the first row

        # insert tables
        placeholders = ', '.join(['?'] * len(headers))
        insert_sql = f'INSERT OR IGNORE INTO {table_name} ({", ".join(headers)}) VALUES ({placeholders})'

        # insert rows
        for row in reader:
            cursor.execute(insert_sql, row)
    conn.commit()
    conn.close()
    print(f"Loaded data from {tsv_file_path} into {table_name} table.")

db_name = f'models/omop/omop_full.db'

# stepp 1: creat the tables
load_sql_files_in_order(db_name, sql_files)

# Step 2: load data
path = f'example-data/omop/full_tables'
for i in tables:
    print( os.path.join(path,f'omop_{i}.tsv'))
    load_tsv_to_table(db_name, os.path.join(path,f'omop_{i}.tsv'), i)
