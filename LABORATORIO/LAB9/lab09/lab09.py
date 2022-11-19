#JULIO ANTHONY ENGELS RUIZ COTO - 1284719
#LABORATORIO # 9
from flask import *
import queue
'''
def insertar_nuevo():
  archivo = open("lab09/basedatos.txt", 'a')
  insertar = input('Inserte nuevo registro: ')
  archivo.write(insertar + "\n")
  archivo.close()

def leer_ultimo():
  with open('lab09/basedatos.txt', 'r') as f:
    for line in f:
        pass #actua como una linea en blanco 
    last_line = line
  print(last_line)

def borrar_contenido():
  archivo =  open('lab09/basedatos.txt', 'r+')
  archivo.truncate(0) # need '0' when using r+
  print("----El archivo esta vacio----")
'''
app = Flask(__name__) #initialize web application
#post -> create , get -> obtener , delete

@app.route("/")
def principio():
  return "<-------------------CONEXION EXITOSA :)-------------------->"

@app.route('/insertar/<registro>', methods=['POST', 'GET'])
def Insert(registro):
        archivo = open('/home/JR1284719/Desktop/basedatos.txt','a' )
        archivo.write(registro + "\n")
        archivo.close()
        return "<-----------Se ha insertado correctamente----------->"


@app.route('/leer' , methods=['GET'])
def Read():
    with open('/home/JR1284719/Desktop/basedatos.txt', 'r') as Last:
        last_line = Last.readlines()[-1]
    print(last_line)
    return "<----------------El último registro del archivo es: "+ last_line


@app.route('/eliminar', methods=['GET'])
def Delete():
    open('/home/JR1284719/Desktop/basedatos.txt','w').close()
    return "<----------------Se borro el archivo.txt--------------->"
    
if __name__ == '__main__':
  app.run(debug=True)