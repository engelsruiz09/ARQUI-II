#LABORATORIO 4
#alumno JULIO ANTHONY ENGELS RUIZ COTO - 1284719 
import RPi.GPIO as GPIO #Biblioteca phyton control de los GP
import time
GPIO.setmode(GPIO.BCM) # define modo de numeracion 
GPIO.setwarnings(False)  #desactiva los mensajes de alerta

GPIO.setup(16, GPIO.IN) #Este pin es una entrada.
GPIO.setup(20, GPIO.OUT) # este pin es de salida
GPIO.setup(21, GPIO.OUT) # este pin es de salida


while True:
    while True:
            inputvalor = GPIO.input(16)
            if(inputvalor == True):
                GPIO.output(20, True)       #enciende led 1
                GPIO.output(21, False)      #apaga led 2
                print("Se ha presionado la tecla 1" , end = "\r")
                time.sleep(0.4)
                break
    while True:
            inputvalor = GPIO.input(16)
            if(inputvalor == True):
                GPIO.output(20, False)     #apaga led 1
                GPIO.output(21, True)      #enciende led 2
                print("Se ha presionado la tecla 2", end = "\r")
                time.sleep(0.4)
                break
