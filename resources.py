# Importamos la clase Resource
# Resource es un molde que permite que una clase
# sea usada por el servidor para dar respuestas
from operator import index

from flask_restful import Resource

from flask import make_response, render_template


# Un recurso representa algo que el servidor puede responder
# Para crear un recurso, se crea una clase que hereda de Resource
# Esto le dice al servidor: "esta clase puede responder mensajes"
class HolaMundo(Resource):

    # Resource revisa esta clase y busca funciones con nombres especiales
    # Si encuentra una función llamada get, entiende lo siguiente:
    # "Cuando alguien pida información en este punto,
    # ejecuta esta función y responde con lo que regrese"
    def get(self):
        return {"hola": "mundo"}


class PantallaInicio(Resource):

    # Esta función describe qué va a responder este recurso
    # Piensa: “si alguien llega aquí, ¿qué le contesto?”
    # No importa todavía cómo llega, solo qué respuesta doy
    def get(self):

        #renderizamos el contenido del archivo html
        content = render_template('index.html')

        #retornamos el contenido renderizado en una respuesta
        return make_response(content)


class Despedida(Resource):

    # Esta función define la respuesta de este recurso
    # Todo lo que esté dentro se ejecuta antes de responder
    # print sirve solo para mostrar mensajes en la consola del servidor
    # return es lo que realmente se envía como respuesta al exterior
    def get(self):
        print("Esto es un texto de prueba")
        return "Adios"
