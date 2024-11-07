from flask import Flask, request, jsonify
from cohortPhenopackets import phenopacketsReturnData
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/cohortRetrieval')
def listTools():
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