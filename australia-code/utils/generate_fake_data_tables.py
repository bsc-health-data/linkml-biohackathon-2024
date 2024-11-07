import redivis
import numpy as np
import sys
import pandas as pd

# Usage: python3 generate_fake_data_tables.py 100

user = redivis.user("demo")
dataset = user.dataset("cms_synthetic_patient_data_omop:ye2v:v2_0")
count = sys.argv[1] # Number of fake data rows to generate.
dest = 'example-data/omop'

##########################################################################################
############################## CONTAINER TABLE
##########################################################################################

# CREATE TABLE "Container" (
# 	id INTEGER NOT NULL, 
# 	PRIMARY KEY (id)
# );
container = pd.DataFrame([[1]], columns=['id'])
print(container)
container.to_csv(f"{dest}/omop_minimal_db_container.tsv", index = False, sep = '\t')

##########################################################################################
############################## PERSON TABLE
##########################################################################################

# CREATE TABLE "Person" (
# 	person_id INTEGER NOT NULL, 
# 	year_of_birth INTEGER, 
# 	gender_concept_id INTEGER, 
# 	"Container_id" INTEGER, 
# 	PRIMARY KEY (person_id), 
# 	FOREIGN KEY("Container_id") REFERENCES "Container" (id)
# );
query = dataset.query(f"""
    SELECT person_id, gender_concept_id, year_of_birth FROM person:cdwn 
    LIMIT {count};
""")
person = query.to_pandas_dataframe()
person = person[['person_id', 'year_of_birth', 'gender_concept_id']]
person['Container_id'] = 1
print(person)
person.to_csv(f"{dest}/omop_minimal_db_person.tsv", index = False, sep = '\t')
##########################################################################################
############################## CONDITION OCCURENCE TABLE
##########################################################################################

#CREATE TABLE "Condition_occurrence" (
# 	condition_occurrence_id INTEGER NOT NULL, 
# 	person_id INTEGER, 
# 	condition_source_value TEXT, 
# 	"Container_id" INTEGER, 
# 	PRIMARY KEY (condition_occurrence_id), 
# 	FOREIGN KEY("Container_id") REFERENCES "Container" (id)
# );

df = pd.DataFrame(person['person_id'].tolist(), columns=['person_id'])
print(df)
df['condition_occurrence_id'] = np.random.randint(0, 1001, size=len(person))
df['condition_source_value'] = np.random.randint(1, 9999, size=len(person))
df['Container_id'] = 1
df = df[['condition_occurrence_id', 'person_id', 'condition_source_value', 'Container_id']]
print(df)

df.to_csv(f"{dest}/omop_minimal_db_condition_occurrence.tsv", index = False, sep = '\t')