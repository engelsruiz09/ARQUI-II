from distutils.log import debug
import RPi._GPIO as GPIO
import pyrebase
import time
from datetime import datetime
from flask import Flask, render_template

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
contadorinterup = 0

dataon = {"Fecha y hora": str(datetime.now()),
                "Usuario": "JR1284719@raspberrypi",
                "Estado_LED": "ON"}
dataoff = {"Fecha y hora": str(datetime.now()),
                "Usuario": "JR1284719@raspberrypi",
                "Estado_LED": "OFF"}
def insertar(conta):
    if(conta == 1):
        db.child("Estado").child("Estado_LED_ON").push(dataon)
        
    else:
       db.child("Estado").child("Estado_LED_OFF").push(dataoff)
        
app = Flask(__name__)#initialize web application

@app.route('/on')
def on():
    GPIO.output(21, True)       #enciende led 1
    time.sleep(0.8)
    insertar(1)
    return render_template('on.html')

@app.route('/off')
def off():
    GPIO.output(21, False)       #apaga led 1
    time.sleep(0.8)
    insertar(0)
    return render_template('off.html')

  