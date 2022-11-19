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
auth = firebase.auth()

app = Flask(__name__) #initialize web application
@app.route('/', methods=['GET','POST'])
def basic():
  noexitoso = 'Porfavor verifique sus credenciales'
  exitoso = 'Inicio de sesion exitosa'
  if request.method == 'POST':
    email = request.form['name']
    password = request.form['pass']
    try:
      #auth.sign_in_with_email_and_password(email,password)
      db.child("Authentication").push(email)
      db.child("Authentication").push(password)
      return render_template('au.html', s = exitoso)
    except:
      return render_template('au.html',ne = noexitoso)
  return render_template('au.html')

if __name__ == '__main__':
  app.run()