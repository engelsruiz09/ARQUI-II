#JULIO ANTHONY ENGELS RUIZ COTO - 1284719
#EDDIE ALEJANDRO GIRON CARRANZA - 1307419
from crypt import methods
import RPi._GPIO as GPIO
import pyrebase
import time
from datetime import datetime
from flask import *
import statistics
import pandas as pd
import numpy as np
import statistics


now=datetime.now()
df = pd.DataFrame()
GPIO.setmode(GPIO.BCM) # define modo de numeracion 
GPIO.setwarnings(False)  #desactiva los mensajes de alerta

    
GPIO.setup(23, GPIO.IN) #Este pin es una entrada(6).
GPIO.setup(24, GPIO.IN) #Este pin es una entrada(7).

GPIO.setup(25, GPIO.IN) #Este pin es una entrada(0).
GPIO.setup(8, GPIO.IN) #Este pin es una entrada(1).
GPIO.setup(7, GPIO.IN) #Este pin es una entrada(2).
GPIO.setup(1, GPIO.IN) #Este pin es una entrada(3).
GPIO.setup(12, GPIO.IN) #Este pin es una entrada(4).
GPIO.setup(16, GPIO.IN) #Este pin es una entrada(5).
GPIO.setup(20, GPIO.IN) #Este pin es una entrada(6).
GPIO.setup(21, GPIO.IN) #Este pin es una entrada(7).

def count(list1, low, high): 
    c = 0   
    for x in list1:      
        if x>= low and x<= high: 
            c+= 1 
    return c

def count2(list2, low, high): 
    c = 0  
    for x in list2:      
        if x>= low and x>= high: 
            c+= 1 
    return c 

contdatos = 0
contseg=0
lista = []
tiempo = []
SUMA = 0
cont0_100=0
cont101_200=0
cont201_300=0
cont301_400=0
cont401_500=0
cont501_600=0
cont601_700=0
cont701_800=0
cont801_900=0
cont901_1000=0
cont1001_1024=0
cont = 0

app = Flask(__name__) #initialize web application

@app.route('/', methods=['GET','POST'])
def inicio():
   return render_template('indicex2.html')

@app.route('/Datos', methods=['GET','POST'])
def basic():
   global contseg
   global SUMA 
   global lista
   global tiempo
   global cont0_100
   global cont101_200
   global cont201_300
   global cont301_400
   global cont401_500
   global cont501_600
   global cont601_700
   global cont701_800
   global cont801_900
   global cont901_1000
   global cont1001_1024
   global cont
   if request.method == 'POST':
      if request.form['submit'] == 'delete':
         contseg=0
         cont=0
         lista = []
         lista.clear()
         tiempo = []
         SUMA = 0
         cont0_100=0
         cont101_200=0
         cont201_300=0
         cont301_400=0
         cont401_500=0
         cont501_600=0
         cont601_700=0
         cont701_800=0
         cont801_900=0
         cont901_1000=0
         cont1001_1024=0

   if GPIO.input(23) == True:
      time.sleep(0.1)
      SUMA+=1

   if GPIO.input(24) == True:
      time.sleep(0.1)
      SUMA+=2

   if GPIO.input(25) == True:
      time.sleep(0.1)
      SUMA+=4
               
   if GPIO.input(8) == True:
      time.sleep(0.1)
      SUMA+=8

   if GPIO.input(7) == True:
      time.sleep(0.1)
      SUMA+=16
               
   if GPIO.input(1) == True:
      time.sleep(0.1)
      SUMA+=32

   if GPIO.input(12) == True:
      time.sleep(0.1)
      SUMA+=64

   if GPIO.input(16) == True:
      time.sleep(0.1)
      SUMA+=128

   if GPIO.input(20) == True:
      time.sleep(0.1)
      SUMA+=256
            
   if GPIO.input(21) == True:
      time.sleep(0.1)
      SUMA+=512
   cont+=5
   print(SUMA)
   lista.append(SUMA)
   string1 = str(datetime.now())
   string2 = str(datetime.now())
   tiempo.append(cont)
   #tiempo.append(now.time())
   SUMA = 0

         
   #df = pd.DataFrame(list(zip(tiempo,lista)), columns = ['Hora','Niv.Luz'])

   string1 = str(datetime.now())
   string2 = str(datetime.now())
   valor_max= str(max(lista)) + " " + "/ Hora: " + string1[11:25]
   valor_min= str(min(lista)) + " " + "/ Hora: "  + string2[11:25]
   promedio= statistics.mean(lista)


   print("-------")   
   print("valor maximo es:" ,valor_max)     
   print("valor minimo es:" ,valor_min)
   print("valor promedio es:", promedio)
   print("-------") 
   low=0
   high=100
   cont0_100= count(lista, low, high)
   print("cont0_100 es:",cont0_100)
   low=101
   high=200
   cont101_200=count(lista, low, high)
   print("cont101_200 es:",cont101_200)
   low=201
   high=300
   cont201_300=count(lista, low, high)
   print("cont201_300 es:",cont201_300)
   low=301
   high=400
   cont301_400=count(lista, low, high)
   print("cont301_400 es:",cont301_400)          
   low=401
   high=500
   cont401_500=count(lista, low, high)
   print("cont401_500 es:",cont401_500)
   low=501
   high=600
   cont501_600=count(lista, low, high)
   print("cont501_600 es:",cont501_600)
   low=601
   high=700
   cont601_700=count(lista, low, high)
   print("cont601_700 es:",cont601_700)
   low=701
   high=800
   cont701_800=count(lista, low, high)
   print("cont701_800 es:",cont701_800)
   low=801
   high=900
   cont801_900=count(lista, low, high)
   print("cont801_900 es:",cont801_900)
   low=901
   high=1000
   cont901_1000=count2(lista, low, high)
   print("cont901_1000 es:",cont901_1000)
   low=1001
   high=1024
   cont1001_1024=count2(lista, low, high)
   print("cont1001_1024 es:",cont1001_1024)


   
   return render_template('indicex.html',lista=lista,tiempo=tiempo, valor_max = valor_max, valor_min = valor_min, promedio = promedio,cont0_100=cont0_100,cont101_200=cont101_200,cont201_300=cont201_300,cont301_400=cont301_400,cont401_500=cont401_500,cont501_600=cont501_600,cont601_700=cont601_700,cont701_800=cont701_800,cont801_900=cont801_900,cont901_1000=cont901_1000,cont1001_1024=cont1001_1024)
   
if __name__ == '__main__':
  app.run(debug=True)