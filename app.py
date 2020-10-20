from flask import Flask, render_template,request,redirect,url_for, Response
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost/prospectos'
mongo = PyMongo(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/listado', methods = ['GET'])
def listado():
    prospectos = mongo.db.prospectos.find({})
    return render_template('listado.html', prospectos = prospectos)

@app.route('/evaluacion', methods = ['GET'])
def evaluacion():
    prospectos = mongo.db.prospectos.find({})
    return render_template('evaluacion.html', prospectos = prospectos)

if __name__ == '__main__':
    app.run(debug=True)