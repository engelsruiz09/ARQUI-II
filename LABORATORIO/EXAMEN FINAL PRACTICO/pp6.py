import RPi.GPIO as GPIO
import time
from os import system
from datetime import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  #desactiva los mensajes de alerta
#sensor delantero
GPIO.setup(20, GPIO.IN)  #se conecta al sensor de proximidad IRF Front derecho
GPIO.setup(26, GPIO.IN)  #se conecta al sensor de proximidad IRF Front izquierdo

#mandos motor rueda 1
GPIO.setup(14, GPIO.OUT) # este pin es de salida: pin 2 ,L293D
GPIO.setup(15, GPIO.OUT) # este pin es de salida: pin 7 ,L293D
#mandos motor rueda 2
GPIO.setup(2, GPIO.OUT) # este pin es de salida: pin 15 ,L293D 
GPIO.setup(3, GPIO.OUT) # este pin es de salida: pin 10 ,L293D

#Usamnos Modulacion por acho de pulso PWM en ambos motores
# para que no se acelere tanto y darle tiempo a los sensores
# de proximidad para que detecten. Si lleva mucha velocidad
# por la inercia del carrito no para instantaneamente.

#pwm motor rueda 1
GPIO.setup(17, GPIO.OUT) # este pin es de salida: pin 1 ,L293D
pwm1 = GPIO.PWM(17,19)
pwm1.start(0)

#pwm motor rueda 2
GPIO.setup(18, GPIO.OUT) # este pin es de salida: pin 1 ,L293D
pwm2 = GPIO.PWM(18,24)
pwm2.start(0)

# Rutina Movercarro(x)
# x = "0" mueve carrito hacia adelante.
# x = "1" mueve carrito hacia atras.
# x = "2" carrito en stop.

def Movercarro(x):
    if x == 0:       #motor de rueda hacia adelante
           #motor rueda 1 
       GPIO.output(14,True)
       GPIO.output(15,False)
       #motor rueda 2
       GPIO.output(2,True)
       GPIO.output(3,False)
       print('rueda 1 y rueda 2 adelante')
       
    elif x==1:          #motor de rueba retroceso
             #motor rueda 1  
             GPIO.output(14,False)
             GPIO.output(15,True)
             #motor rueda 2
             GPIO.output(2,False)
             GPIO.output(3,True)
             print('rueda 1 y rueda 2 reversa')
                        
             
    else:  # se usa x=2 para condicion de paro 
          #motor rueda 1 
       GPIO.output(14,False)
       GPIO.output(15,False)
        #motor rueda 2
       GPIO.output(2,False)
       GPIO.output(3,False)
       print('rueda 1 y rueda 2 stop')
       
#Rutina Cruzar(x)
# x = "3" movimiento a la izquierda
# x = "4" movimiento a la derecha       
# se aumenta la velocidad para tratar de que la vuelta la de mas rapido       
def Cruzar (x):
    pwm1.ChangeDutyCycle(90)
    pwm2.ChangeDutyCycle(90)
    if x== 3:  # cruzar izquierda
       
       GPIO.output(14,False)   #mover rueda 1
       GPIO.output(15,True)
            #motor rueda 2 reversa
       GPIO.output(2,True)
       GPIO.output(3,False)
       time.sleep(3)
     
       print("cruzar izquierda")
       
    elif x==4:  #cruzar derecha
        #mover rueda 2 
        GPIO.output(2,False)
        GPIO.output(3,True)
        
        GPIO.output(14,True)   #mover rueda 1 reversa
        GPIO.output(15,False)
        time.sleep(3)
        print("cruzar derecha")
#Rutina para evitar obstaculos        
def Obstaculo (y):
    if y==0:
        Cruzar(4)       #cruzar a la derecha
        time.sleep(30)
        Movercarro(0)   #mueve carrito
        time.sleep(2)
        Movercarro(2)   #para carrito
        Cruzar(3)       #cruzar a la izquierda
        Movercarro(2)
        Movercarro(0)   #avanza carrito
        time.sleep(4)
        Movercarro(2)   #para carrito
        Cruzar(3)       #cruzar izquierda
        Movercarro(2)
        Movercarro(0)   #avanza carrito
        time.sleep(2)
        Cruzar(4)       #cruzar derecha 
        
#Rutina para la velocidad normal del carrito sin obstaculos 
def Vel_norm() :
     pwm1.ChangeDutyCycle(19) 
     pwm2.ChangeDutyCycle(24)    
   
       

#pwm1.ChangeDutyCycle(22) #modulando el PWM (modulacion por ancho de pulso) se baja velocidad al carrito
#pwm2.ChangeDutyCycle(19) #para ambas ruedas por si fuera muy rapido
    

n=0 #cambiar esto a 0 luego de llegar a meta
#coordenadas sobre la matriz 
x=0    #fila
y=0    #columna

tiempoI=datetime.now()
tiempoi = time.time()
 
try:

     while True:
          if n == 0:
              Movercarro(2)
#------------------------------------------x = 0, y = 0---------------------------------
          if n == 1 and x==0 and y==0:     #posicion inicial x=0 y=0
              Vel_norm()
              Movercarro(0)   # mueve carrito desde posicion inicial a lo largo de eje x
              tiempo_0F =  time.time()
              tiempo_0 = tiempo_0F-tiempoi
              # desplazamiento (d) = velocidad lineal*tiempo_
              d_0= 14*tiempo_0
              print("d =" , d_0)
              print(tiempo_0)
              
          if GPIO.input(26) == 0 or GPIO.input(20) == 0:      #si detecta pared lateral fin de x=4 y=0
              tiempoF = datetime.now()
              tiempo = tiempoF-tiempoI
              print("tiempo = " , tiempo)
                          
 #------------------------------------------x = 4, y = 0---------------------------------             
              print("x=4,y=0")
              Movercarro(2) #para el carrito
              n=n+1
              print(n)
          if n==2:
              Cruzar(3)     #cruzar a la izquierda
              time.sleep(2)
              Movercarro(2)
              n=n+1
          if n==3:
              Vel_norm()
              Movercarro(0)
              time.sleep(4)
              n=n+1
              y= y+1
#------------------------------------------x = 4, y = 1---------------------------------
              print("x = 4, y = 1")
          if n == 4:                     #posicion x=4 y=1
              Movercarro(2)
              Cruzar(3)     #cruzar a la izquierda
              time.sleep(4)
              Movercarro(2)
              n=n+1
              tiempoi = time.time()
          if n == 5:
              Vel_norm()
              Movercarro(0)   # mueve carrito
              
              tiempo_1F =  time.time()
              tiempo_1 = tiempo_1F-tiempoi
              d_1 = 14*tiempo_1
              print("d = -" , d_1)
              
              #verificar si hay obstaculo
          if GPIO.input(20) == 0 or GPIO.input(26) == 0 :   #posicion x = 0, y = 1
#------------------------------------------x = 0, y = 1---------------------------------              
              print("x = 0, y = 1" )
              Movercarro(2) #para el carrito
              n=n+1
          if n==6:               
             Cruzar(4)       #cruzar a la derecha
             time.sleep(6)
             Movercarro(2)
             n=n+1
             y = n+1
            
          if n==7   :
             Vel_norm() 
             Movercarro(0)
             time.sleep(4)
             print("x = 0, y = 2")
#------------------------------------------x = 0, y = 2---------------------------------             
             Cruzar(4)       #cruzar a la derecha
             time.sleep(6)
             Movercarro(2)
             n =n+1
             tiempoi = time.time()
          if n ==8:
             Vel_norm() 
             Movercarro(0)
             
             tiempo_2F =  time.time()
             tiempo_2 = tiempo_2F-tiempoi
             d_2 = 14*tiempo_2
             print("d = " , d_2)
             
          if GPIO.input(20) == 0 or GPIO.input(26) == 0 :   #posicion x = 4, y = 2  
             print("x=4,y=2")
             Movercarro(2) #para el carrito
             n=n+1
          if n==9:
              Cruzar(3)     #cruzar a la izquierda
              time.sleep(2)
              Movercarro(2)
              n=n+1
          if n==10:
              Vel_norm()
              Movercarro(0)
              time.sleep(3)
              n=n+1
              y= y+1
              print("x=4,y=3")
 #------------------------------------------x = 4, y = 3---------------------------------             
          if n ==11:
              Cruzar(3)     #cruzar a la izquierda
              time.sleep(2)
              Movercarro(2)
              n=n+1
              tiempoi = time.time()
          if n == 12:
              Vel_norm()
              Movercarro(0)
              
              tiempo_3F = time.time()
              tiempo_3 = tiempo_3F-tiempoi
              d_3 = 14*tiempo_3
              print("d = - " , d_3)
              
          if GPIO.input(20) == 0 or GPIO.input(26) == 0 :   #posicion x = 0, y = 3  
             print("x=0,y=3")
             Movercarro(2) #para el carrito llego meta     
             print("x=0,y=3")
             print("OVERGAME")
         
        
except:
    GPIO.cleanup()
    
       
            
