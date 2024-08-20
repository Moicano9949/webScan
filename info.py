#!/usr/bin/env python3
import subprocess
import platform
import socket
import uuid
import shutil
import os
import urllib.request
import json
import pyaudio
import cv2
import locale

def obtener_nombre_red_wifi():
    sistema = platform.system()

    if sistema == "Linux":
        try:
            resultado = subprocess.check_output(["iwgetid", "-r"]).strip()
            nombre_red_wifi = resultado.decode("utf-8")
            print(f"Nombre de la red WiFi: {nombre_red_wifi}")
        except subprocess.CalledProcessError:
            print("No se pudo obtener el nombre de la red WiFi.")
    
    elif sistema == "Windows":
        try:
            resultado = subprocess.check_output(["netsh", "wlan", "show", "interfaces"], shell=True).decode("latin-1")
            nombre_red_wifi = [line.split(":")[1].strip() for line in resultado.splitlines() if "SSID" in line]
            print(f"Nombre de la red WiFi: {nombre_red_wifi[0]}")
        except subprocess.CalledProcessError:
            print("No se pudo obtener el nombre de la red WiFi.")

    elif sistema == "Darwin":
        try:
            resultado = subprocess.check_output(["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-I"]).decode("utf-8")
            nombre_red_wifi = [line.split(":")[1].strip() for line in resultado.splitlines() if "SSID" in line]
            print(f"Nombre de la red WiFi: {nombre_red_wifi[0]}")
        except subprocess.CalledProcessError:
            print("No se pudo obtener el nombre de la red WiFi.")

    elif sistema == "Android":
        try:
            resultado = subprocess.check_output(["dumpsys", "wifi"]).decode("utf-8")
            nombre_red_wifi = [line.split(":")[1].strip() for line in resultado.splitlines() if "SSID" in line]
            print(f"Nombre de la red WiFi: {nombre_red_wifi[0]}")
        except subprocess.CalledProcessError:
            print("No se pudo obtener el nombre de la red WiFi en Android.")

    elif sistema == "iOS":
        try:
            resultado = subprocess.check_output(["iwconfig"]).decode("utf-8")
            nombre_red_wifi = [line.split('"')[1].strip() for line in resultado.splitlines() if "ESSID" in line]
            print(f"Nombre de la red WiFi: {nombre_red_wifi[0]}")
        except subprocess.CalledProcessError:
            print("No se pudo obtener el nombre de la red WiFi en iOS.")

    else:
        print("No se admite la obtención del nombre de la red WiFi en este sistema operativo.")

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
def obtener_info_microfonos():
    p = pyaudio.PyAudio()

    num_dispositivos = p.get_device_count()
    print(f"Total de dispositivos de audio: {num_dispositivos}")

    for i in range(num_dispositivos):
        info_dispositivo = p.get_device_info_by_index(i)
        
        if info_dispositivo['maxInputChannels'] > 0:
            print(f"\nInformación del micrófono {i + 1}:")
            print(f"Nombre: {info_dispositivo['name'].encode('latin-1').decode('utf-8')}")
            print(f"Índice: {info_dispositivo['index']}")
            print(f"Canales de entrada: {info_dispositivo['maxInputChannels']}")
            print(f"Frecuencia de muestreo predeterminada: {info_dispositivo['defaultSampleRate']} Hz")
            print(f"Descripción adicional: {info_dispositivo['hostApi']}")
            print("-" * 30)

    p.terminate()

def obtener_info_camaras():
    camaras = []

    for i in range(10):
        cap = cv2.VideoCapture(i)

        if cap.isOpened():
            camaras.append(f"Camara {i + 1}")
            cap.release()

    if not camaras:
        print("No se encontraron cámaras disponibles.")
        return

    print(f"Total de cámaras disponibles: {len(camaras)}")

    for camara_nombre in camaras:
        print(f"\nInformación de {camara_nombre}:")
        cap = cv2.VideoCapture(camaras.index(camara_nombre))
        print(f"Resolución predeterminada: {int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))}x{int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))}")
        print(f"FPS predeterminado: {int(cap.get(cv2.CAP_PROP_FPS))}")
        cap.release()

def obtener_info_teclado():
    idioma_sistema, _ = locale.getdefaultlocale()
    print(f"Idioma del sistema: {idioma_sistema}")

def obtener_info_sistema():
    sistema = platform.system()
    version_sistema = platform.version()
    nombre = platform.node()
    procesador = platform.processor()

    print(f"Sistema: {sistema} - Versión: {version_sistema}")
    print(f"Nombre del nodo: {nombre}")
    print(f"Procesador: {procesador}")
    ip = obtener_ip()
    ubicacion = obtener_ubicacion(ip)
    print("Ubicación aproximada basada en la dirección IP pública:")
    print(f"IP: {ip}")
    print(f"Ciudad: {ubicacion.get('city', 'Desconocido')}")
    print(f"Región: {ubicacion.get('region', 'Desconocido')}")
    print(f"País: {ubicacion.get('country', 'Desconocido')}")
    print(f"Coordenadas: {ubicacion.get('loc', 'Desconocido')}")

    try:
        direccion_ip = socket.gethostbyname(socket.gethostname())
        print(f"Dirección IP: {direccion_ip}")
    except socket.gaierror:
        print("No se pudo obtener la dirección IP.")

    try:
        direccion_ipv6 = socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET6)[0][4][0]
        print(f"Dirección IPv6: {direccion_ipv6}")
    except (socket.gaierror, IndexError):
        print("No se pudo obtener la dirección IPv6.")

    try:
        direccion_mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(5, -1, -1)])
        print(f"Dirección MAC: {direccion_mac}")
    except Exception as e:
        print(f"No se pudo obtener la dirección MAC. Error: {e}")

    total, usado, libre = shutil.disk_usage("/")
    print(f"Almacenamiento total: {total / (2**30):.2f} GB")
    print(f"Almacenamiento usado: {usado / (2**30):.2f} GB")
    print(f"Almacenamiento libre: {libre / (2**30):.2f} GB")
    print(f"ruta: {os.getcwd()}")

if __name__ == "__main__":
    obtener_info_sistema()
    obtener_info_teclado()
    obtener_nombre_red_wifi()
    obtener_info_microfonos()
    obtener_info_camaras()