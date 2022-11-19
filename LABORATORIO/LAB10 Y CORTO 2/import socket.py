#este codigo era con el fin de conectar el microfono en nuestra laptop y mandar los comandos desde la laptop a la raspi pero no funciono
#las librerias en windows ni en ubuntu
import speech_recognition as sr
import socket 

a = sr.Recognizer()

s = socket.socket()
s.connect(("192.168.1.**",2020))
while True:
  try:
    with sr.Microphone() as source:
         print("<-----Hable algo------>")
         audio = a.listen(source)
         data = a.recognize_google(audio, language = 'es-ES')
         s.send(data.encode())

  except:
    print("No se entiende")


#el siguiente codigo va en la raspi
'''
import socket

s = socket.socket()
s.bind(("192.168.1.**",2020))
s.listen(10)
print("Esperando conexiones...")
(sc,addrc) = s.accept()
print("Cliente conectado",addrc)
continuar = True
while continuar:
    dato = sc.recv(64)
    if not dato:
        continuar = False
        print("Cliente desconectado")
    else:
        print(dato)
sc.close()
s.close()
print("Fin de programa")
'''
  



