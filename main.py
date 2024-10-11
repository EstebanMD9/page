from flask import Flask
import random

app = Flask(__name__)
facts_list = ["La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos",
"Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones",
"El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna"]

@app.route("/")
def index():
    return f'<h1>Hola me llamo esteban</h1>'

@app.route("/datos")
def facts():
    return f'<p>{random.choice(facts_list)}</p>'

app.run(debug=True)