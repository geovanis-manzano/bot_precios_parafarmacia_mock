import requests
import json
import pandas as pd
import logging

class Parafarmacia:
    def __init__(self, config, token):
        # URL del servicio web Parafarmacia
        self.url_parafarmacia = config['api_urls']['parafarmacia_url']
        
        # Encabezados de la solicitud
        self.headers = {
            'Authorization': f'Bearer {token}',
            'Accept': 'application/json'
        }
        
        # Parámetros de la solicitud
        self.params = config['parametros_parafarmacia']
        
        # Ruta para guardar el archivo Excel
        self.output_path = config['output_path_parafarmacia']        

    def descargar_parafarmacia(self):
        logger = logging.getLogger()
        
        # Realizar la solicitud GET
        # print("Descargando parafarmacia ...")
        logger.info("Descargando parafarmacia ...")
        
        respuesta_parafarmacia = '''
        {
        "Titulo":"Búsqueda avanzada",
        "Resultados":[
            {
                "Id":167668,
                "Codigo":"1617477",
                "NombreCompleto":"+ DEFENS  10 VIALES 11 ml",
                "CodTipoRegistro":"PPF",
                "TipoRegistro":"Productos alimenticios",
                "PVPIVA":0.0,
                "PFacturacion":0.0,
                "PVL":0.0,
                "IdEstadoAutorizacion":"0",
                "EstadoAutorizacion":"Comercializado",
                "IdLaboratorio":9451,
                "Laboratorio":"SORIA NATURAL",
                "FechaAlta":"2011-06-22T00:00:00",
                "ProblemaSuministro":"",
                "Financiado":"N",
                "Receta":"MSR",
                "Notificado":null,
                "AmbitoHospitalario":null,
                "ImagenEnvase":{
                    "IdDocumento":182976,
                    "Titulo":"1617477.jpg",
                    "IdTipo":43,
                    "Tipo":"IMAGENES PARAFARMACIA: FOTO ENVASES",
                    "URL":"http://botplusweb.farmaceuticos.com//Documentos/MasivaParafarmacia/167668/1617477.jpg",
                    "URLFull":null,
                    "OrdenTipo":32,
                    "idAux":167668,
                    "Fecha":"0001-01-01T00:00:00"
                },
                "FechaVisita":"0001-01-01T00:00:00",
                "FechaFinPS":"0001-01-01T00:00:00",
                "NombreAnterior":null,
                "AuxInt":0,
                "AuxStr":null,
                "AuxStr2":null,
                "AuxStr3":null,
                "AuxDbl":0.0,
                "AuxFecha":"0001-01-01T00:00:00",
                "AuxFecha2":"0001-01-01T00:00:00",
                "ListaAux1":null,
                "ListaAux2":null,
                "ListaStr":null,
                "ListaIntolerancias":[
                    2,
                    5,
                    24
                ]
            },
            {
                "Id":167669,
                "Codigo":"1617484",
                "NombreCompleto":"+DEFENS JUNIOR  10 VIALES 11 ml",
                "CodTipoRegistro":"PPF",
                "TipoRegistro":"Productos alimenticios",
                "PVPIVA":0.0,
                "PFacturacion":0.0,
                "PVL":0.0,
                "IdEstadoAutorizacion":"0",
                "EstadoAutorizacion":"Comercializado",
                "IdLaboratorio":9451,
                "Laboratorio":"SORIA NATURAL",
                "FechaAlta":"2011-06-22T00:00:00",
                "ProblemaSuministro":"",
                "Financiado":"N",
                "Receta":"MSR",
                "Notificado":null,
                "AmbitoHospitalario":null,
                "ImagenEnvase":{
                    "IdDocumento":183109,
                    "Titulo":"1617484.jpg",
                    "IdTipo":43,
                    "Tipo":"IMAGENES PARAFARMACIA: FOTO ENVASES",
                    "URL":"http://botplusweb.farmaceuticos.com//Documentos/MasivaParafarmacia/167669/1617484.jpg",
                    "URLFull":null,
                    "OrdenTipo":32,
                    "idAux":167669,
                    "Fecha":"0001-01-01T00:00:00"
                },
                "FechaVisita":"0001-01-01T00:00:00",
                "FechaFinPS":"0001-01-01T00:00:00",
                "NombreAnterior":null,
                "AuxInt":0,
                "AuxStr":null,
                "AuxStr2":null,
                "AuxStr3":null,
                "AuxDbl":0.0,
                "AuxFecha":"0001-01-01T00:00:00",
                "AuxFecha2":"0001-01-01T00:00:00",
                "ListaAux1":null,
                "ListaAux2":null,
                "ListaStr":null,
                "ListaIntolerancias":[
                    2,
                    5,
                    24
                ]
            }
        ],
        "Completo":true,
        "Total":45599,
        "IdBusqueda":397040,
        "AuxDbl":0.0,
        "AuxDbl2":0.0,
        "AuxStr":null,
        "AuxStr2":null,
        "Mensaje":null
        }
        ''' 

        # print("Descarga de parafarmacia completada con exito")
        logger.info("Descarga de parafarmacia completada con exito")

        # Convertir la respuesta a un diccionario de Python
        respuesta_parafarmacia_diccionario = json.loads(respuesta_parafarmacia)

        # Acceder a la sección "Resultados"
        resultados = respuesta_parafarmacia_diccionario["Resultados"]

        # Crear un DataFrame de pandas con los datos
        df = pd.DataFrame(resultados)
        
        # Eliminar el símbolo '+' al inicio del campo "NombreCompleto", ya sea con o sin espacio
        df['NombreCompleto'] = df['NombreCompleto'].str.lstrip('+ ').str.lstrip('+')

        # Guardar el DataFrame en un archivo Excel
        df.to_excel(self.output_path, index=False)

        # print(f"Datos almacenados en {self.output_path}")
        logger.info(f"Datos almacenados en {self.output_path}")
