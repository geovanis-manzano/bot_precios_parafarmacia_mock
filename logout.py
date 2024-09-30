import requests
import logging

class Logout:
    def __init__(self, config, token):
        # URL del servicio web Logout
        self.url_logout = config['api_urls']['logout_url']
        
        # Encabezados de la solicitud
        self.headers = {
            'Authorization': f'Bearer {token}'
        }      

    def cerrar_sesion(self):
        logger = logging.getLogger()
        
        # Realizar la solicitud POST
        respuesta_logout = ''        
       
        # print('La sesión de BotPlus ha sido cerrada exitosamente')
        logger.info('La sesión de BotPlus ha sido cerrada exitosamente')
        