from crypt import methods
import RPi._GPIO as GPIO
import pyrebase
import time
from datetime import datetime
from flask import *

GPIO.setmode(GPIO.BCM) # define modo de numeracion 
GPIO.setwarnings(False)  #desactiva los mensajes de alerta

GPIO.setup(21, GPIO.OUT) # este pin es de salida

name = '5'

for i in range(0, int(name)):
        GPIO.output(21, False)
        time.sleep(0.8)
        GPIO.output(21, True)
        time.sleep(0.8)
GPIO.output(21,False)