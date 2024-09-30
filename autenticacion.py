import requests
import json
import logging

class Autenticacion:
    def __init__(self, config):
        # URL del servicio web Login
        self.url_autenticacion = config['api_urls']['autenticacion_url']
        
        # Datos que se envian en la solicitud POST
        self.credenciales = config['credenciales_autenticacion']        

    def obtener_token(self):        
        # Realizar la solicitud POST
        # print("Realizando autenticacion ...")
        logger = logging.getLogger()
        logger.info("Realizando autenticacion ...")
        
       # Respuesta del servicio de autenticación
        respuesta_autenticacion = '''
        {
            "botPlusUser": {
                "Username": "bpm117329",
                "idCCAA": 13,
                "CCAA": "Madrid",
                "idProvincia": 28,
                "Provincia": "Madrid",
                "SessionStatus": 0,
                "Rol": "CLI",
                "HaAceptadoLicencia": true,
                "LicenciaAAceptar": "Licencia.pdf",
                "LicenciaHasta": null,
                "EsUsuarioPrincipal": true
            },
            "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6ImJwbTExNzMyOSIsInJvbGUiOiJDbGllbnRlIiwiaWRTZXNpb24iOiIyNzM2MDY1IiwiaWRDQ0FBIjoiMTMiLCJpZFN1YnNlc2lvbiI6IjAiLCJuYmYiOjE3MTMyNjM4NDMsImV4cCI6MTcxMzMyMTQ0MywiaWF0IjoxNzEzMjYzODQzLCJpc3MiOiJodHRwOi8vbG9jYWxob3N0IiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdCJ9.iHWQ4rvEceNztUIY3qaQIeNd5bfUPCqqkmMlWPGY8nE",
            "Status": 0,
            "Mensaje": null,
            "Info": null
        }
        '''
        
        # print("Autenticacion completada con exito")
        logger.info("Autenticacion completada con exito")

        # Convertir la respuesta a un diccionario de Python
        respuesta_diccionario = json.loads(respuesta_autenticacion)

        # Extraer el token de autenticación
        token = respuesta_diccionario['Token']
        # print(f"Token: {token}")
        logger.info(f"Token: {token}")