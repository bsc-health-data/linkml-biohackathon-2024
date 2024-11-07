import sys
import yaml

# cohortVariables = ['diseases','subject']

def retrieveAgeSex(yamlData):
    ageList =[]
    sexDict = {}
    if 'subject' in yamlData:
        if 'sex' in yamlData['subject']:
            if yamlData['subject']['sex'] in sexDict:
                sexDict[yamlData['subject']['sex']] += 1
            else:
                sexDict[yamlData['subject']['sex']] = 1
        if 'timeAtLastEncounter' in yamlData['subject']:
            if 'age' in yamlData['subject']['timeAtLastEncounter']:
                ageISO = yamlData['subject']['timeAtLastEncounter']['age']['iso8601duration']
                ageISO = ageISO.replace('P','')
                ageISO = ageISO.replace('Y','')
                ageList.append(ageISO)
    return {'age':int(ageISO), 'sex':sexDict}

def retrieveDiseases(yamlData):
    diseasesDict = {}
    if 'diseases' in yamlData:
        for diseasesTerms in yamlData['diseases']:
            diseasesDict[diseasesTerms['term']['id']] = diseasesTerms['term']['label']
    return {'diseases':diseasesDict}

def retrieveCohortdata(yamlData):
    ageSexCohort = retrieveAgeSex(yamlData)
    diseasesCohort = retrieveDiseases(yamlData)
    return {**ageSexCohort, **diseasesCohort}

# Function to return cohort phenopackets data
def phenopacketsReturnData(filepath):
    with open(filepath, 'r') as yamlFile:
        yamlData = yaml.safe_load(yamlFile)
        cohortdata = retrieveCohortdata(yamlData)
    return cohortdata


# Example
# http://127.0.0.1:5000/cohortRetrieval?model=Phenopackets&path=/home/sergi/Desktop/BSC/Biohackaton/DataModel/extractCohort/data/Phenopacket-acute-myeloid-leukemia.yaml