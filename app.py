#el botón de encendido


#importamos flask para crear el servidor
from  flask import Flask

#importamos restful para indicar que recursos(info/respuesta) será capaz de arrojar
#importamos la clases API Y Resource de Flask-RESTful.
#Api: organiza los recursos y las rutas
#Resource: permite que una clase responda peticiones
from flask_restful import Api, Resource
from routes import create_routes


#Creamos el servidor y lo guardamos en el  objeto app de clase Flask
#Flask es el molde con la infraestructura del server
#el parametro __name__ solo se coloca porque es necesario para funcionar.
#__name__ inidca desde que archivo se esta creando el servidor
app = Flask(__name__)

#Creamos la API en el objeto "api" de clase API y como argumento le pasamos como parametro  el server
#La API será el programa que se comunique con el servidor(dispositivo físico)
#Api es una clase (modelo) que le da la capacidad al server de responder con orden y con reglas REST (GET,POST,PUT,DELETE)
api = Api(app)

#Agrega las rutas(caminos) posibles a la API
#create_routes es una funcion que se crea en routes.py
#es necesario mandarla a llamar la funcion ya que si no error el archivo routes
create_routes(api)

#ejecutamos el metodo run que enciende un servidor local (app)
#port= es el puerto local donde se escuchará el servidor
#debug= True muestra en pantalla errores claros
app.run(port=8081, debug= True)
#127.0.0.1:8081 LoopBack |  IP local
