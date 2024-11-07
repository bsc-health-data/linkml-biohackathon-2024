from linkml.validator import validate
from linkml_map.session import Session
from linkml.utils.schema_builder import SchemaBuilder
import random
from datetime import datetime
from pydantic import ConfigDict

def map_standard_to_omop(standard_model_data: dict) -> dict:
  maleConceptId = 1
  femaleConceptId = 2
  otherConceptId = 0

  person_occurence_session = Session()
  person_occurence_session.set_source_schema('models/cohort/cohort.yml')
  person_occurence_session.set_object_transformer(f"""
    class_derivations:
      Person_occurence:
        populated_from: DataDictionary
        slot_derivations:
          person_id:
            range: integer
            expr: {random.randint(1, 1000)}
          year_of_birth:
            range: integer
            expr: {datetime.now().year} - {{age}}
          gender_concept_id:
            range: integer
            expr: {maleConceptId} if {{sex}} == 'Male' else {femaleConceptId} if {{sex}} == 'Female' else {otherConceptId}
          condition_source_value:
            populated_from: disease
    """)

  person_occurence_sb = SchemaBuilder()
  for person_occurence_class in person_occurence_session.target_schemaview.schema.classes.values():
    person_occurence_sb.add_class(
      person_occurence_class.name,
      slots=person_occurence_class.attributes.values(),
    )

  person_occurence_sb.add_defaults()

  person_session = Session()
  person_session.set_source_schema(person_occurence_session.target_schemaview.schema)
  person_session.set_object_transformer(f"""
    class_derivations:
      Person:
        populated_from: Person_occurence
        slot_derivations:
          person_id:
            populated_from: person_id
          year_of_birth:
            populated_from: year_of_birth
          gender_concept_id:
            populated_from: gender_concept_id
    """)

  condition_occurence_session = Session()
  condition_occurence_session.set_source_schema(person_occurence_session.target_schemaview.schema)
  condition_occurence_session.set_object_transformer(f"""
    class_derivations:
      Condition_occurrence:
        populated_from: Person_occurence
        joins:
          alias: Person
          class_named: Person
        slot_derivations:
          condition_occurrence_id:
            expr: {random.randint(1, 1000)}
          condition_source_value:
            populated_from: condition_source_value
          person_id:
            populated_from: person_id
    """)

  person_occurence = person_occurence_session.transform(standard_model_data)
  return {
    'person': person_session.transform(person_occurence),
    'condition_occurence': condition_occurence_session.transform(person_occurence),
  }

def map_standard_to_fhir(standard_model_data: dict) -> dict:

  codable_concept_session = Session()
  codable_concept_session.set_source_schema('models/cohort/cohort.yml')
  codable_concept_session.set_object_transformer(f"""
    class_derivations:
      CodableConcept:
        populated_from: DataDictionary
        slot_derivations:
          text:
            populated_from: disease
    """)

  condition_session = Session()
  condition_session.set_source_schema('models/cohort/cohort.yml')
  condition_session.set_object_transformer(f"""
    class_derivations:
      Condition:
        populated_from: DataDictionary
        slot_derivations:
          id:
            range: integer
            expr: str({random.randint(1, 1000)})
          code:
            expr: None
          subject:
            expr: None
          onsetDateTime:
            range: integer
            expr: {datetime.now().year} - {{age}}
    """)
  
  patient_session = Session()
  patient_session.set_source_schema('models/cohort/cohort.yml')
  patient_session.set_object_transformer(f"""
    class_derivations:
      Patient:
        populated_from: DataDictionary
        slot_derivations:
          id:
            range: string
            expr: str({random.randint(1, 1000)})
          gender:
            expr: sex
          birthDate:
            range: integer
            expr: {datetime.now().year} - {{age}}
    """)

  condition = condition_session.transform(standard_model_data);
  condition['subject'] = patient_session.transform(standard_model_data)
  condition['code'] = codable_concept_session.transform(standard_model_data)
  return condition

def convert_to_standard(standard_model_data: dict, model_name: str) -> dict:
  report = validate(standard_model_data, 'models/cohort/cohort.yml', 'DataDictionary')
  for r in report.results:
    if r.severity == 'ERROR':
      raise Exception(r.message)
    
  if model_name == 'OMOP':
    return map_standard_to_omop(standard_model_data)
  if model_name == 'FHIR':
    return map_standard_to_fhir(standard_model_data)
  else:
    raise Exception(f'Unknown model name: {model_name}')
  
def convert_fhir_to_standard(data: dict):
  session = Session()
  session.set_source_schema('models/fhir/fhir_linkml_mvp.yml')
  report = validate(data, 'models/fhir/fhir_linkml_mvp.yml', 'Container')
  session.set_object_transformer(f"""
    class_derivations:
      DataDictionary:
        populated_from: Condition
        slot_derivations:
          age:
            expr: onsetDateTime - subject.birthDate
            range: integer
          gender:
            expr: subject.gender
            range: string
          disease:
            expr: code.text
            range: string
      Container:
        name: Container
        populated_from: Container
        slot_derivations:
          persons:
            name: persons
            populated_from: conditions
    """)
  print(session.target_schema)
  mapped_data = session.transform(data)
  print(mapped_data)
  return mapped_data
