import yaml
import json

def checkId(patient):
    if 'id' in patient:
        id = patient['id']
    return id

def checkAge(patient,  minageVar, maxageVar):
    if 'subject' in patient:
        if 'timeAtLastEncounter' in patient['subject']:
            if 'age' in patient['subject']['timeAtLastEncounter']:
                ageISO = patient['subject']['timeAtLastEncounter']['age']['iso8601duration']
                ageISO = ageISO.replace('P','')
                ageISO = ageISO.replace('Y','')
                ageISO = int(ageISO)
                if ageISO > int(minageVar)  and ageISO < int(maxageVar):
                    return ageISO
                return False

def checkSex(patient, sexVar):
    if 'subject' in patient:
        if 'sex' in patient['subject']:
            sex= patient['subject']['sex']
            if sex in sexVar:
                return sex
            return False

def checkDisease(patient, diseaseVar):
    # listDiseases = []
    if 'diseases' in patient:
        for diseasesTerms in patient['diseases']:
            disease = diseasesTerms['term']['label']
            if disease in diseaseVar:
                return disease
            return False

def retrieveCohortdata(rawData, sexVar,  minageVar, maxageVar, diseaseVar):
    listPatients = []
    for patient in rawData:
        subjectId = checkId(patient)
        age = checkAge(patient,  minageVar, maxageVar)
        if age is False:
            continue
        sex = checkSex(patient, sexVar)
        if sex is False:
            continue
        disease = checkDisease(patient, diseaseVar)
        if disease is False:
            continue
        listPatients.append({'age': age, 'sex': sex, 'disease': disease, 'subject_id': subjectId})
    cohortLinkMLData = {'subjects': listPatients}
    return cohortLinkMLData

def retrieveDataPhenopackets(pathFile, sexVar, minageVar, maxageVar, diseaseVar):
    with open(pathFile, 'r') as rawFile:
        if pathFile.endswith('.yaml') or pathFile.endswith('.yml'):
            jsonData = yaml.safe_load(rawFile)
        else:   #json
            jsonData = json.load(rawFile)
        cohortLinkMLData = retrieveCohortdata(jsonData, sexVar,  minageVar, maxageVar, diseaseVar)    
    return cohortLinkMLData