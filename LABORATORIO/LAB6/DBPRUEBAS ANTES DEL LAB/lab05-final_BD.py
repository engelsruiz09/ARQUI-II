#JULIO ANTHONY ENGELS RUIZ COTO - 1284719
#LABORATORIO # 5
#EMISOR - RECEPTOR
import RPi.GPIO as GPIO
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

#cargar el certificado del proyecto 
firebase_SDK = credentials.Certificate("key.json")
#hace referencia a la base de datos en tiempo real de firebase
firebase_admin.initialize_app(firebase_SDK, {'databaseURL':'https://raspi-f08b6-default-rtdb.firebaseio.com/'})
#crear una coleccion 

ref = db.reference("/Interrupcion_corta o Interrupcion_larga")
def insertar(conta):
    tiempo = datetime.now()
    if(conta == 1):
        ref.push({        
                    "Fecha y hora": str(tiempo),
                    "Proceso": "Interupcion_corta",     
                    })
        
    else:
        ref.push({        
                    "Fecha y hora": str(tiempo),
                    "Proceso": "Interrupcion_larga: {0:.3f}" .format(cont)
                    })

# 0 es con interrupcion
# 1 es sin interrupcion
try:
    while True:
        tiempo = datetime.now()
        if GPIO.input(16) == 0:
            while GPIO.input(16) == 0:
               time.sleep(0.1)
               cont += 0.1
               
            if cont < 1:
                GPIO.output(21,1)             
                print("Se ha producido una interrupcion corta" + ' ' + str(tiempo))
                insertar(1)
                time.sleep(0.9)
                GPIO.output(21,0)
                
            else:
                GPIO.output(21,1)
                print("Se realizó una interrupcion larga {0:.3f}" .format(cont),  str(tiempo))
                insertar(0)
                time.sleep(0.9)
                GPIO.output(21,0)
                
        cont = 0        
except KeyboardInterrupt:
    GPIO.cleanup()