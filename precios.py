import requests
import json
import pandas as pd
import logging

class PreciosMedicamentos:    
    def __init__(self, config, token):
        # URL del servicio web Medicamentos Precios
        self.url_precios = config['api_urls']['medicamentos_precios_url']
        
        # Encabezados de la solicitud
        self.headers = {
            'content-type': 'application/json; charset=utf-8',
            'Authorization': f'Bearer {token}'
        }
        
        # Datos a enviar en la solicitud (en formato JSON)
        self.data = {
            "tipoRegistros": "MUH",
            "ids": config['ids_precios'],
            "campos": config['campos_precios'],
            "campoOrden": "NOMMUH"
        }
        
        # Ruta para guardar el archivo Excel
        self.output_path = config['output_path_precios']        

    def descargar_precios(self):
        logger = logging.getLogger()
        
        # Realizar la solicitud POST
        # print("Descargando precios de medicamentos ...")
        logger.info("Descargando precios de medicamentos ...")
        
        # Respuesta del servicio Medicamentos Precios
        respuesta_medicamentos_precios = '''
        {
            "cabeceras":[
                {
                    "label":"Código nacional",
                    "key":"CNMUH"
                },
                {
                    "label":"Nombre",
                    "key":"NOMMUH"
                },
                {
                    "label":"Descripción",
                    "key":"DESMUH"
                },
                {
                    "label":"PVL",
                    "key":"PVLMUH"
                },
                {
                    "label":"PVP con IVA",
                    "key":"PVPMUH"
                },
                {
                    "label":"Precio facturación",
                    "key":"PFAMUH"
                }
            ],
            "datos":[
                {
                    "ESPEUNIC":88084.0,
                    "CNMUH":6001141.0,
                    "NOMMUH":"PENTOTHAL SODICO",
                    "DESMUH":"1 g 50 VIALES",
                    "PVLMUH":"66,64",
                    "PVPMUH":"81,06",
                    "PFAMUH":null
                },
                {
                    "ESPEUNIC":88086.0,
                    "CNMUH":6008744.0,
                    "NOMMUH":"RAUDOPEN",
                    "DESMUH":"500 mg 500 CAPSULAS",
                    "PVLMUH":"71,92",
                    "PVPMUH":"87,48",
                    "PFAMUH":null
                },
                {
                    "ESPEUNIC":88098.0,
                    "CNMUH":6011874.0,
                    "NOMMUH":"NEOPENYL 1 MILLON",
                    "DESMUH":"100 VIALES",
                    "PVLMUH":"123",
                    "PVPMUH":"149,61",
                    "PFAMUH":null
                }
            ]
        }
        '''

        # print("Descarga de precios de medicamentos completada con exito")
        logger.info("Descarga de precios de medicamentos completada con exito")

        # Convertir la respuesta a un diccionario de Python
        respuesta_medicamentos_precios_diccionario = json.loads(respuesta_medicamentos_precios)

        # Acceder a la sección "datos"
        datos = respuesta_medicamentos_precios_diccionario["datos"]

        # Crear un DataFrame de pandas con los datos
        df = pd.DataFrame(datos)

        # Reemplazar comas por puntos en las columnas PVLMUH y PVPMUH
        df['PVLMUH'] = df['PVLMUH'].str.replace(',', '.')
        df['PVPMUH'] = df['PVPMUH'].str.replace(',', '.')

        # Guardar el DataFrame en un archivo Excel
        df.to_excel(self.output_path, index=False)

        # print(f"Datos almacenados en {self.output_path}")
        logger.info(f"Datos almacenados en {self.output_path}")
        