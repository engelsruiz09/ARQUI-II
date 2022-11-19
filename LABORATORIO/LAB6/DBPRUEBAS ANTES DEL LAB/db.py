import pyrebase
import time
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


#cargar el certificado del proyecto 
firebase_SDK = credentials.Certificate("keylab06.json")
#hace referencia a la base de datos en tiempo real de firebase
firebase_admin.initialize_app(firebase_SDK, {'databaseURL':'https://labemisor-default-rtdb.firebaseio.com/'})

ref = db.reference("/primer nodo")
data = {"Age": 21, "name": "Julio","apellido": "Ruiz"}
ref.set(data)

ref = db.reference("/segundo nodo")
tiempo = datetime.now()
ref.set(str(tiempo))

ref = db.reference("/primer nodo")
ref.update({"name":"ramires"})

ref = db.reference("/segundo nodo")
ref.update({
            "tipoint1":"corta",
            "tipoint2":"larga: " + str(tiempo)
            })

#ref.child("tipoint2").delete()
def pruebadeenvioaterminal():
  prueba = ref.get({
            "tipoint1":"corta",
            "tipoint2":"larga: " + str(tiempo)
            })
  print(prueba)

ref = db.reference("/segundo nodo")
pruebadeenvioaterminal()
