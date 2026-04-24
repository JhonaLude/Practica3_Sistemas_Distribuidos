from flask import Flask, render_template, jsonify

from ejercicios.mutex import ejecutar_mutex
from ejercicios.semaforo import ejecutar_semaforo
from ejercicios.productor_consumidor import ejecutar_pc
from ejercicios.lectores_escritores import ejecutar_le
from ejercicios.barrera import ejecutar_barrera

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/mutex")
def mutex():
    return jsonify({"resultado": ejecutar_mutex()})

@app.route("/semaforo")
def semaforo():
    return jsonify({"resultado": ejecutar_semaforo()})

@app.route("/pc")
def pc():
    return jsonify({"resultado": ejecutar_pc()})

@app.route("/le")
def le():
    return jsonify({"resultado": ejecutar_le()})

@app.route("/barrera")
def barrera():
    return jsonify({"resultado": ejecutar_barrera()})

if __name__ == "__main__":
    app.run(debug=True)