from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def home():
    return 'hello'


@app.route('/barrios', methods=['GET'])
def get_barrios():
    barrios = {"barrios": [{"nombre": "Belen", "ubicacion": "occidente"},
                           {"nombre": "America", "ubicacion": "Sur Occidente"},
                           {"nombre": "Calasanz", "ubicacion": "Norte"}]}
    return barrios


@app.route('/barrios', methods=['POST'])
def add_barrios():
    barrios = {"barrios": [{"nombre": request.json['nombre'], "ubicacion": request.json['ubicacion']}]}
    return barrios
