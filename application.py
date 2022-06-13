from flask import Flask, request
import requests
import os

app = Flask(__name__)


@app.route('/')
def home():
    return 'Variabes de Productividad'

@app.route('/barrios', methods=['GET'])
def get_barrios():
    url = 'https://6285ace696bccbf32d6678b3.mockapi.io/api/v1/barrios'
    response = requests.get (url, {}, timeout=5 )
    return  {"barrios": response.json() }

@app.route('/barrios', methods=['POST'])
def add_variables():
    url = 'https://6285ace696bccbf32d6678b3.mockapi.io/api/v1/barrios'
    response = requests.post (url, {request}, timeout=5 )
    variables = {"barrios": [{"nombre": response.json["nombre"], "ubicacion": response.json["ubicacion"], "id": response.json["id"]}]}
    return variables

@app.route('/clima', methods=['GET'])
def get_clima():
    url = 'https://api.openweathermap.org/data/3.0/onecall?lat=6.25027313614039&lon=-75.58314414533237&exclude=hourly,daily&appid=34392a979659233359b419555c04c9d8'
    response = requests.get (url, {}, timeout=5 )
    return  {"clima": response.json() }


@app.route('/variables', methods=['GET'])
def get_variables():
    variables = {"variables": [{"nombre": "Comunicacion", "tipo": "Blanda", "descripcion":"Comunicacion"},
                                {"nombre": "Coordinacion de expertos", "tipo": "Blanda", "descripcion":"Coordinacion de expertos"},
                                {"nombre": "Cohesion", "tipo": "Blanda", "descripcion":"Cohesion"},
                                {"nombre": "Confianza", "tipo": "Blanda", "descripcion":"Confianza"},
                                {"nombre": "Soporte mutuo", "tipo": "Blanda", "descripcion":"Soporte mutuo"},
                                {"nombre": "Compromiso total de gestion ", "tipo": "Blanda", "descripcion":"Compromiso total de gestion "},
                                {"nombre": "Gestion de personas ", "tipo": "Blanda", "descripcion":"Gestion de personas "},
                                {"nombre": "Enfoque al cliente ", "tipo": "Blanda", "descripcion":"Enfoque al cliente "},
                                {"nombre": "Soporte organizacional ", "tipo": "Blanda", "descripcion":"Soporte organizacional "},
                                {"nombre": "Orientacion a los objetivos", "tipo": "Blanda", "descripcion":"Orientacion a los objetivos"},
                                {"nombre": "Estructura informal", "tipo": "Blanda", "descripcion":"Estructura informal"},
                                {"nombre": "Resolucion de problemas en equipo", "tipo": "Blanda", "descripcion":"Resolucion de problemas en equipo"},
                                {"nombre": "Especificacion funcional", "tipo": "Blanda", "descripcion":"Especificacion funcional"},
                                {"nombre": "Vision de equipo", "tipo": "Blanda", "descripcion":"Vision de equipo"},
                                {"nombre": "Relacion entre equipos", "tipo": "Blanda", "descripcion":"Relacion entre equipos"},
                                {"nombre": "Funcionalidad", "tipo": "Blanda", "descripcion":"Funcionalidad"},
                                {"nombre": "Independencia", "tipo": "Blanda", "descripcion":"Independencia"},
                                {"nombre": "Comprension", "tipo": "Blanda", "descripcion":"Comprension"},
                                {"nombre": "Gastos administrativos", "tipo": "otro", "descripcion":"Gastos administrativos"},
                                {"nombre": "Valor compartido o de diversidad", "tipo": "Tecnica", "descripcion":"Valor compartido o de diversidad"},
                                {"nombre": "Efectividad", "tipo": "Tecnica", "descripcion":"Efectividad"},
                                {"nombre": "Eficiencia", "tipo": "Tecnica", "descripcion":"Eficiencia"},
                                {"nombre": "Mejora continua ", "tipo": "Tecnica", "descripcion":"Mejora continua "},
                                {"nombre": "Orientacion a la innovacion ", "tipo": "Tecnica", "descripcion":"Orientacion a la innovacion "},
                                {"nombre": "Tasa de defectos", "tipo": "Tecnica", "descripcion":"Tasa de defectos"},
                                {"nombre": "Líneas de codigo por persona en un día", "tipo": "Tecnica", "descripcion":"Líneas de codigo por persona en un día"},
                                {"nombre": "Especificacion de diseño", "tipo": "Tecnica", "descripcion":"Especificacion de diseño"},
                                {"nombre": "Revision del diseño", "tipo": "Tecnica", "descripcion":"Revision del diseño"},
                                {"nombre": "Revision del codigo", "tipo": "Tecnica", "descripcion":"Revision del codigo"},
                                {"nombre": "Subciclos", "tipo": "Tecnica", "descripcion":"Subciclos"},
                                {"nombre": "Prototipo", "tipo": "Tecnica", "descripcion":"Prototipo"},
                                {"nombre": "Construccion diaria", "tipo": "Tecnica", "descripcion":"Construccion diaria"},
                                {"nombre": "Pruebas de regresion", "tipo": "Tecnica", "descripcion":"Pruebas de regresion"},
                                {"nombre": "Velocidad de equipo", "tipo": "Tecnica", "descripcion":"Velocidad de equipo"},
                                {"nombre": "Conformidad de la calidad", "tipo": "Tecnica", "descripcion":"Conformidad de la calidad"},
                                {"nombre": "Manejo de requisitos por parte del equipo", "tipo": "Tecnica", "descripcion":"Manejo de requisitos por parte del equipo"},
                                {"nombre": "Complejidad", "tipo": "Tecnica", "descripcion":"Complejidad"},
                                {"nombre": "Calidad", "tipo": "Tecnica", "descripcion":"Calidad"},
                                {"nombre": "horas hombre", "tipo": "Tecnica", "descripcion":"horas hombre"},
                                {"nombre": "Abstraccion", "tipo": "Tecnica", "descripcion":"Abstraccion"},
                                {"nombre": "Líneas de codigo por tiempo", "tipo": "Tecnica", "descripcion":"Líneas de codigo por tiempo"},
                                {"nombre": "Esfuerzo realizado por tiempo", "tipo": "Tecnica", "descripcion":"Esfuerzo realizado por tiempo"},
                                {"nombre": "Codigo propio por tiempo", "tipo": "Tecnica", "descripcion":"Codigo propio por tiempo"},
                                {"nombre": "Commits por tiempo", "tipo": "Tecnica", "descripcion":"Commits por tiempo"},
                                {"nombre": "Líneas commits por tiempo", "tipo": "Tecnica", "descripcion":"Líneas commits por tiempo"},
                                {"nombre": "Caracteres commits por tiempo", "tipo": "Tecnica", "descripcion":"Caracteres commits por tiempo"}]}
    return variables


@app.route('/variables', methods=['POST'])
def add_variables():
    variables = {"variables": [{"nombre": request.json["nombre"], "tipo": request.json["tipo"], "descripcion": request.json["descripcion"]}]}
    return variables

port = os.environ.get("PORT", 5000)
# print('get port %d' % port)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
