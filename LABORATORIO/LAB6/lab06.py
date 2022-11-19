import RPi._GPIO as GPIO
import pyrebase
import time
from os import system
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

GPIO.setmode(GPIO.BCM) # define modo de numeracion 
GPIO.setwarnings(False)  #desactiva los mensajes de alerta

GPIO.setup(16, GPIO.IN) #Este pin es una entrada.
GPIO.setup(21, GPIO.OUT) # este pin es de salida
cont = 0
contint = 1
conttres = 0

#cargar el certificado del proyecto 
firebase_SDK = credentials.Certificate("key.json")
#hace referencia a la base de datos en tiempo real de firebase
firebase_admin.initialize_app(firebase_SDK, {'databaseURL':'https://raspi-f08b6-default-rtdb.firebaseio.com/'})

#crear una coleccion
ref = db.reference("/Lab06/Operacion")

cont1 = 0
contadorinterup = 0

try:
    while True:
        if GPIO.input(16) == 0:
            cont1 = cont1 + 1
            contadorinterup += 1
            print("Se ha interrumpido", contadorinterup)
            time.sleep(0.5)
            GPIO.output(21,1)
            time.sleep(0.1)
            GPIO.output(21,0)
            
        if cont1 == 3:
            ref.push({
                "Fecha y hora": str(datetime.now()),
                "Usuario": "JR1284719@raspberrypi",
                "Interrupcion": contadorinterup
                })

            cont1 = 0        
except KeyboardInterrupt:
    GPIO.cleanup()
