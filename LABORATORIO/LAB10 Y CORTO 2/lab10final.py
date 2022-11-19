#el microfono se conecta ala raspi y desde ahi se mandan los comandos de voz pip install pyaudio pip install SpeechRecognition pip install google-api-python-client

import speech_recognition as sr 
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM) # define modo de numeracion 
GPIO.setwarnings(False)  #desactiva los mensajes de alerta

GPIO.setup(16, GPIO.OUT)  # este pin es de salida
GPIO.setup(19, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(20, GPIO.OUT) # este pin es de salida
GPIO.setup(21, GPIO.OUT) # este pin es de salida
GPIO.setup(26, GPIO.IN) # este pin es entrada
GPIO.setup(20,GPIO.IN)

a = sr.Recognizer()
while True:
   try:
      with sr.Microphone() as source:
         print("<-----Hable algo------>")
         audio = a.listen(source)
         data = a.recognize_google(audio, language = 'es-ES')
         print (data)
      if data == "Encender luz uno" or data =="Encender luz 1":
         GPIO.output(16,1)

      if data == "Apagar luz uno" or data =="Apagar luz 1":
          GPIO.output(16,GPIO.LOW)

      if data == "Encender luz dos" or data =="Encender luz 2":
         GPIO.output(19,1)

      if data == "Apagar luz dos" or data =="Apagar luz 2":
          GPIO.output(19,GPIO.LOW)

      if data == "Encender luz tres" or data =="Encender luz 3":
         GPIO.output(17,1)

      if data == "Apagar luz tres" or data =="Apagar luz 3":
         GPIO.output(17,GPIO.LOW)

      if data == "parar" or data == "Parar":
         break

      if data == "receptor" or data == "Receptor":
         while True:
            if GPIO.input(26) == 0:
               GPIO.output(16,GPIO.HIGH)
               break
            if GPIO.input(20) == 0:
               GPIO.output(19,GPIO.HIGH)
               break
   except:
      print("<---No se entiende---->")