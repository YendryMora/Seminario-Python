"""================================================================================================ 
Institucion..: Universidad Tecnica Nacional Sede.........: Del Pacífico 
Carrera......: Tecnologías de la Información Periodo......: 1-2018 Charla.......: 
Introduccion a Python Documento....: api_01.py Objetivos....: Creación de micro 
servicios web (api-REST) Encargado....: Jorge Ruiz (york) Estudiante...: 
================================================================================================"""

## Configura el reconocimiento de caracteres especiales en caso de la plataforma Linux es_CR.utf8
import locale
#locale.setlocale(locale.LC_ALL,"es")

## Librería que permite crear la aplicación web, talves sea necesario instalar la librería por
## medio del comando pip install flask en la terminal
from flask import Flask
app = Flask(__name__)

## Crea la ruta a seguir, similar a /var/www/
@app.route('/')

## Define la pagina principal del sitio
def index():
    return 'Hola mundo.....(york)!'

## Presenta información en consola sobre lo que realiza la aplicación
if __name__ == '__main__':
	app.run(host='10.90.30.210', port=5001, debug=True)




