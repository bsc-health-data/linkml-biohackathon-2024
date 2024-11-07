import yaml
import json

# cohortVariables = ['diseases','subject']

def retrieveAgeSex(patient, ageList, sexDict):
    if 'subject' in patient:
        if 'sex' in patient['subject']:
            if patient['subject']['sex'] in sexDict:
                sexDict[patient['subject']['sex']] += 1
            else:
                sexDict[patient['subject']['sex']] = 1
        if 'timeAtLastEncounter' in patient['subject']:
            if 'age' in patient['subject']['timeAtLastEncounter']:
                ageISO = patient['subject']['timeAtLastEncounter']['age']['iso8601duration']
                ageISO = ageISO.replace('P','')
                ageISO = ageISO.replace('Y','')
                ageList.append(ageISO)
    return ageList, sexDict

def retrieveDiseases(patient, diseasesDict):
    if 'diseases' in patient:
        for diseasesTerms in patient['diseases']:
            diseasesDict[diseasesTerms['term']['id']] = diseasesTerms['term']['label']
    return diseasesDict

def retrieveCohortdata(rawData):
    ageList =[]
    sexDict = {}    
    diseasesDict = {}
    for patient in rawData:
        ageList, sexDict = retrieveAgeSex(patient, ageList, sexDict)
        diseasesDict = retrieveDiseases(patient, diseasesDict)
    return {'age':ageList, 'sex':sexDict, 'diseases':diseasesDict}

# Function to return cohort phenopackets data
def phenopacketsReturnData(filepath):
    with open(filepath, 'r') as rawFile:
        if filepath.endswith('.yaml') or filepath.endswith('.yml'):
            jsonData = yaml.safe_load(rawFile)
        else:   #json
            jsonData = json.load(rawFile)
        cohortdata = retrieveCohortdata(jsonData)    
    return cohortdata


# Example
# http://127.0.0.1:5000/cohortRetrieval?model=Phenopackets&path=/home/sergi/Desktop/BSC/Biohackaton/DataModel/extractCohort/data/Phenopacket-acute-myeloid-leukemia.yaml