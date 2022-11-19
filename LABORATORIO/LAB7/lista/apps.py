#http://127.0.0.1:5000/
from crypt import methods
import RPi._GPIO as GPIO
import pyrebase
import time
from datetime import datetime
from flask import *

GPIO.setmode(GPIO.BCM) # define modo de numeracion 
GPIO.setwarnings(False)  #desactiva los mensajes de alerta

#GPIO.setup(16, GPIO.IN) #Este pin es una entrada.
GPIO.setup(21, GPIO.OUT) # este pin es de salida

config = {
  "apiKey": "AIzaSyC1NdgkwC1E3DEWphI-Sws4eo3ZmqVF9C8",
  "authDomain": "raspi-f08b6.firebaseapp.com",
  "databaseURL": "https://raspi-f08b6-default-rtdb.firebaseio.com",
  "projectId": "raspi-f08b6",
  "storageBucket": "raspi-f08b6.appspot.com",
  "messagingSenderId": "429206444437",
  "appId": "1:429206444437:web:d7eb8817c98a713db5be9c",
  "measurementId": "G-1HV2MEPE5M"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

app = Flask(__name__) #initialize web application
#GET visible en la barra de direcciones para el usuario, los parametros URL no se envian de nuevo - POST invisible para el usuario, el navegador advierte de que los datos del formulario se enviaran de nuevo
@app.route('/', methods=['GET','POST'])
def basic():
  if request.method == 'POST':
    if request.form['submit'] == 'add':
      name = request.form['name']
      db.child("Hexadecimal").push(name)
      GPIO.output(21, True)       #enciende led 1
      time.sleep(0.4)
      GPIO.output(21, False)       #apaga led 1
      time.sleep(0.4)
      hexa = db.child("Hexadecimal").get()
      hex = hexa.val()
      return render_template('list.html',h = hex.values())

    elif request.form['submit'] == 'delete':
      db.child("Hexadecimal").remove()
    return render_template('list.html')
  return render_template('list.html')

if __name__ == '__main__':
  app.run(debug=True)

