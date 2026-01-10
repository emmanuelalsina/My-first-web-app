# Las rutas de acceso a cada recurso
# Este archivo NO crea el servidor
# Aquí solo se define QUÉ caminos existen y A QUÉ recurso apuntan

'''
app.py crea el servidor y la API
routes.py recibe esa API
y le dice qué rutas (caminos) va a tener
'''

# Importamos los recursos (clases) que saben responder
# Estas clases vienen de resources.py
from resources import *


# Esta función recibe la API ya creada
# La API se pasa como parámetro porque aquí no se crea, solo se usa
def create_routes(api):

    # add_resource sirve para conectar:
    # 1) una clase (recurso)
    # 2) con una dirección (ruta)

    # Cuando alguien entre a /hola
    # la API usará la clase HolaMundo para responder
    api.add_resource(HolaMundo, "/hola")

    # / es la ruta principal (inicio)
    # cuando alguien entra aquí, se usa PantallaInicio
    api.add_resource(PantallaInicio, "/")

    # Cuando alguien entra a /adios
    # la API usa el recurso Despedida
    api.add_resource(Despedida, "/adios")
