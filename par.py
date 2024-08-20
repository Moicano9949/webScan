from urllib.parse import urlparse

def obtener_componentes_url(url):
    parsed_url = urlparse(url)

    esquema = parsed_url.scheme
    url_principal = parsed_url.hostname
    puerto = parsed_url.port if parsed_url.port else 80
    path = parsed_url.path if parsed_url.path else '/'

    print(f"Esquema: {esquema}")
    print(f"URL Principal: {url_principal}")
    print(f"Puerto: {puerto}")
    print(f"Path: {path}")

# Ejemplos
url1 = "http://192.168.1.106:8080"
url2 = "http://192.168.1.106:8080/Login"
url3 = "http://192.168.1.106:8080/ENTER/login"
url4 = "http://192.168.1.106"
url5 = "http://192.168.1.106/Login"

obtener_componentes_url(url1)
obtener_componentes_url(url2)
obtener_componentes_url(url3)
obtener_componentes_url(url4)
obtener_componentes_url(url5)
