""" ================================================================================================
Institucion..: Universidad Tecnica Nacional
Sede.........: Del Pacífico
Carrera......: Tecnologías de la Información
Periodo......: 1-2018
Charla.......: Introducción a Python
Documento....: api_05.py
Objetivos....: Creación de micro servicios web (api-REST)
Encargado....: Jorge Ruiz (york)
Estudiante...:
================================================================================================"""

from flask import Flask, jsonify, abort, make_response, request
app = Flask(__name__)

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

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

##Permite ingresar una nueva tarea a la lista
@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

if __name__ == '__main__':
    app.run(host='10.90.30.210', port=5001, debug=True)
