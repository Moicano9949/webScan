import urllib.request
import json

def obtener_ip():
    url = "http://ipinfo.io/json"
    with urllib.request.urlopen(url) as response:
        data = json.load(response)
        return data.get('ip', '127.0.0.1')

def obtener_ubicacion(ip):
    url = f"http://ipinfo.io/{ip}/json"
    with urllib.request.urlopen(url) as response:
        data = json.load(response)
        return data

if __name__ == "__main__":
    ip = obtener_ip()
    ubicacion = obtener_ubicacion(ip)
    print("Ubicación aproximada basada en la dirección IP pública:")
    print(f"IP: {ip}")
    print(f"Ciudad: {ubicacion.get('city', 'Desconocido')}")
    print(f"Región: {ubicacion.get('region', 'Desconocido')}")
    print(f"País: {ubicacion.get('country', 'Desconocido')}")
    print(f"Coordenadas: {ubicacion.get('loc', 'Desconocido')}")
