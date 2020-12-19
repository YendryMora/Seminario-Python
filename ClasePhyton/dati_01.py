""" ================================================================================================
Institucion..: Universidad Tecnica Nacional
Sede.........: Del Pacifico
Carrera......: Tecnologias de la Informacion
Periodo......: 
Charla.......: Introduccion a Python
Documento....: dati_01.py
Objetivos....: Acceso a bases de datos
Encargado....: Jorge Ruiz (york)
================================================================================================"""

## Libreria para la conexion con MySQL
import MySQLdb

## Declara las variables para la conexion
servidor = 'localhost'
basedatos = 'inventario'
usuario = 'root'
contra = 'parda99'

## Define metodo para ejecutar transaccion
def ejecutar(AuxSql = ''):
    ## crea variable con los datos de conexion
    uri = [servidor, usuario, contra, basedatos]
    
    try:
        ## Intenta conectar con la base de datos
        conex = MySQLdb.connect(*uri)
        
        ## Crea cursor vease como objeto command o statment de otros lenguajes
        cursor = conex.cursor()
        
        ## Ejecuta la instruccion
        cursor.execute(AuxSql)
        
        ## Aplica la transaccion
        conex.commit()
        
        ## Cierra los objetos relacionados con la base de datos
        cursor.close()
        conex.close()
    except Exception as err:
        print('Error: ' + err)

## Define metodo para consultar datos
def consultar(AuxSql = ''):
    ## crea variable con los datos de conexion
    uri = [servidor, usuario, contra, basedatos]
    data = ''
    
    try:
        ## Intenta conectar con la base de datos
        conex = MySQLdb.connect(*uri)
        
        ## Crea cursor vease como objeto command o statment de otros lenguajes
        cursor = conex.cursor()
        
        ## Ejecuta la instruccion
        cursor.execute(AuxSql)
        
        ## Aplica la consulta
        data = cursor.fetchall()
        
        ## Cierra los objetos relacionados con la base de datos
        cursor.close()
        conex.close()
    except Exception as err:
        print('Error: ' + err)
    
    return data

# Define el metodo para insertar datos
def insProducto(nombre, existencia, precio):
    auxSql = "insert into productos(nombre,existencia,precio) values('{0}',{1},{2})".format(nombre, existencia, precio)
    ejecutar(auxSql)

# Define el metodo para insertar datos
def modProducto(nombre, existencia, precio, id ):
    auxSql = "update productos set nombre = '{0}', existencia = {1} ,precio = {2} where id = {3}".format(nombre, existencia, precio, id)
    ejecutar(auxSql)

# Define el metodo para insertar datos
def borProducto(id):
    auxSql = "delete from productos where id = {0}".format(id)
    ejecutar(auxSql)


def imprimir():
    regis = consultar('select * from productos')
    
    for tupla in regis:
        print('Codigo........:{0}'.format(tupla[0]))
        print('Nombre........:{0}'.format(tupla[1]))
        print('Existencia....:{0}'.format(tupla[2]))
        print('Precio........:{0}'.format(tupla[3]))
        print('')
    print('---------------------------------------')
    input('Presione [ENTER] para continuar....!')

# Invoca las rutinas  insercion de datos del cliente
#insProducto('Martillo',  15, 6500)
#insProducto('Cepillo 3"', 7, 18000)
#insProducto('Serrucho',  10, 10000)
imprimir()

modProducto('Cepillo 2"', 8, 14500, 1)
imprimir()

borProducto(1)
imprimir()
