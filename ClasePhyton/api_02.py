""" ================================================================================================
Institucion..: Universidad Tecnica Nacional
Sede.........: Del Pacífico
Carrera......: Tecnologías de la Información
Periodo......: 
Charla.......: Introducción a Python
Documento....: api_02.py
Objetivos....: Creación de micro servicios web (api-REST)
Encargado....: Jorge Ruiz (york)
Estudiante...: Yendry Mora
================================================================================================"""

# Configura el reconocimiento de caracteres especiales
import locale
#locale.setlocale(locale.LC_ALL,"es")

# Librería que permite crear la aplicación web y manipular texto con formato JSON
from flask import Flask, jsonify
app = Flask(__name__)

# Lista de tareas precargadas
tasks = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Beer',
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web',
        'done': False
    }
]

# Genera la lista de las tareas en JSON
@app.route('/tasks', methods=['GET'])

def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(host='10.90.30.210', port=5001, debug=True)


