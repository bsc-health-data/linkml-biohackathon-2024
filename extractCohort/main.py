from flask import Flask, request, jsonify
from cohortPhenopackets import phenopacketsReturnData
from retrievePhenopackets import retrieveDataPhenopackets
from mapping import map_data
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/phenopacketsData')
def phenopacketsData():
    # pathFile = request.args.getlist('routeFile')
    sexVar = request.args.getlist('sex')
    minageVar = request.args.get('minage')
    maxageVar = request.args.get('maxage')

    diseaseVar = request.args.getlist('disease')
    pathFile = request.args.get('path')
    dataModel = request.args.get('model')

    if dataModel=="Phenopackets":
        results = retrieveDataPhenopackets(pathFile, sexVar, minageVar, maxageVar, diseaseVar)
        tr_obj= map_data(results,
                 'models/metaCohortModel.yaml',
                 'CohortData',
                 'models/transformer-common-omop-condition.yaml',
                 'outputfile',
                 'yaml')
    else:
        return {}

    return jsonify(tr_obj)

@app.route('/cohortRetrieval')
def cohortretrieval():
    # pathFile = request.args.getlist('routeFile')
    dataModel = request.args.get('model')
    pathFile = request.args.get('path')

    if dataModel=="Phenopackets":
        results = phenopacketsReturnData(pathFile)
    else:
        return {}

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)