#JULIO ANTHONY ENGELS RUIZ COTO - 1284719
#LABORATORIO # 5
#EMISOR - RECEPTOR
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM) # define modo de numeracion 
GPIO.setwarnings(False)  #desactiva los mensajes de alerta

GPIO.setup(16, GPIO.IN) #Este pin es una entrada.
GPIO.setup(21, GPIO.OUT) # este pin es de salida
cont = 0
# 0 es con interrupcion
# 1 es sin interrupcion
try:
    while True:
        if GPIO.input(16) == 0:
            while GPIO.input(16) == 0:
               time.sleep(0.1)
               cont += 0.1
               
            if cont < 1:
                GPIO.output(21,1)             
                print("Se ha producido una interrupcion")
                time.sleep(0.9)
                GPIO.output(21,0)
                
            else:
                GPIO.output(21,1)
                print("Se realizó una interrupcion larga " , cont)
                time.sleep(0.9)
                GPIO.output(21,0)
                
        cont = 0        
except KeyboardInterrupt:
    GPIO.cleanup()