from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/listado')
def listado():
    return render_template('listado.html')

@app.route('/evalucion')
def evaluacion():
    return render_template('evaluacion.html')

if __name__ == '__main__':
    app.run(debug=True)