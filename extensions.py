
from supabase import create_client

def initiate_db():

    #despues de revisar la documentación esta variable debe recibir: (url,key)
    #La url se obtiene de project settings -> Data API : copiamos el url como primer parámetro de create_client
    #La llave (el 2do parámetro) es la contraseña del proyecto

    # Creamos un cliente de Supabase
    # Este cliente es el que se va a usar para hablar con la base de datos
    # (leer, insertar, actualizar información, etc.)
    client = create_client(supabase_url='https://lversmflpnyvwihaksap.supabase.co',
                           supabase_key = 'sb_publishable_1Y8Q8hTZNwKuTTtMNQ7YZA_Pr7tgqWu') #Dirección del proyecto en Supabase (a qué servidor conectarse)
                                                                                                                        # Llave de acceso (permiso para usar ese proyecto)

    # Devolvemos el cliente ya conectado
    # Quien llame a esta función podrá usar "client" para hacer operaciones en la DB
    return client


