#JULIO ANTHONY ENGELS RUIZ COTO - 1284719
#EDDI ALEJANDRO GIRON CARRANZA - 1307419
#LABORATORIO # 8
#RELAY
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM) # define modo de numeracion 
GPIO.setwarnings(False)  #desactiva los mensajes de alerta

GPIO.setup(16, GPIO.IN) #Este pin es una entrada.
GPIO.setup(21, GPIO.OUT) # este pin es de salida



while True:
  while True:
          inputvalor = GPIO.input(16)
          if(inputvalor == True):
              GPIO.output(21, 1)  
              time.sleep(0.8)
              break
  while True:
          inputvalor = GPIO.input(16)
          if(inputvalor == True):
              GPIO.output(21, 0)  
              time.sleep(0.8)
              break

