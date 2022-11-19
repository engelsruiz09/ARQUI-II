import pyrebase

config = {
    "apiKey": "AIzaSyAOt2-koyg9q_1YSO0_GMTXWjEie9_LF0E",
    "authDomain": "pruebadb-f92d2.firebaseapp.com",
    "projectId": "pruebadb-f92d2",
    "databaseURL": "https://pruebadb-f92d2-default-rtdb.firebaseio.com/",
    "storageBucket": "pruebadb-f92d2.appspot.com",
    "messagingSenderId": "960295438301",
    "appId": "1:960295438301:web:963247c3a228b43b89d834"
  }

firebase = pyrebase.initialize_app(config)
database = firebase.database()

data = {"Age": 21, "name": "Julio","Likes pizza": True}

#----------------------------------------------------------
#create data
#database.push(data)

database.child("Users").child("Primera_persona").set(data)
#----------------------------------------------------------


#----------------------------------------------------------
#read data
#Julio = database.child("Users").child("Primera_persona").get()
#print(Julio.val())
#----------------------------------------------------------

#----------------------------------------------------------
#Update data    
#database.child("Users").child("Primera_persona").update({"name":"Mamerto"})
#----------------------------------------------------------

#----------------------------------------------------------
#remove data
#delete 1 value 

#database.child("Users").child("Primera_persona").child("Age").remove()

#----------------------------------------------------------
#delete whole node
#database.child("Users").child("Primera_persona").remove()

