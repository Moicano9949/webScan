from WebWeaver import WebWeaver

url = 'http://facebook.com'
etiquetas_objetivo = ['title']
opciones_etiquetas = {'title': {'content_only': True}}

resultados = WebWeaver(url, target_tags=etiquetas_objetivo, options=opciones_etiquetas)
if resultados:
    print(f"{resultados[0]}")
else:
    print("No se pudo obtener el título de la página.")
