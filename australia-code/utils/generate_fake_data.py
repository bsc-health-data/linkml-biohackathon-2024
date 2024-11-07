import redivis
import numpy as np
import sys

# Usage: python3 generate_fake_data.py 100

user = redivis.user("demo")
dataset = user.dataset("cms_synthetic_patient_data_omop:ye2v:v2_0")
count = sys.argv[1] # Number of fake data rows to generate.

query = dataset.query(f"""
    SELECT person_id, gender_concept_id FROM person:cdwn 
    LIMIT {count};
""")
person = query.to_pandas_dataframe()

query = dataset.query(f"""
SELECT concept_name FROM concept:w5gj where domain_id = 'Condition' limit {count};
""")
disease =  query.to_pandas_dataframe()

person['disease'] = disease
person['age'] = np.random.randint(0, 101, size=len(person))
person['sex'] = person['gender_concept_id'].apply(lambda x: "Male" if x == 8507 else "Female")
person = person[['person_id', 'age', 'sex', 'disease']]
person.to_csv(f"example-data/omop/omop_example_{count}.tsv", index = False, sep = '\t')