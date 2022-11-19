#http://127.0.0.1:5000/
#LABORATORIO 7
from crypt import methods
import RPi._GPIO as GPIO
import pyrebase
import time
from datetime import datetime
from flask import *

GPIO.setmode(GPIO.BCM) # define modo de numeracion 
GPIO.setwarnings(False)  #desactiva los mensajes de alerta

GPIO.setup(21, GPIO.OUT) # este pin es de salida


app = Flask(__name__) #initialize web application
#GET visible en la barra de direcciones para el usuario, los parametros URL no se envian de nuevo - POST invisible para el usuario, el navegador advierte de que los datos del formulario se enviaran de nuevo
@app.route('/', methods=['GET','POST'])
def basic():
  if request.method == 'POST':
    if request.form['submit'] == 'add':
      name = request.form['name']
      print("En la raspberry ha recibido un dato, el dato recibido es: " + name)
      for i in range(0, int(name)):
        GPIO.output(21, False)
        time.sleep(0.8)
        GPIO.output(21, True)
        time.sleep(0.8)
      GPIO.output(21,False)
      ingreso = input('Ingrese dato para mandar a pag web: ' )
      return render_template('indice.html',ingreso=ingreso)
  return render_template('indice.html')

if __name__ == '__main__':
  app.run(debug=True)
