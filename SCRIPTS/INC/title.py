import requests
from bs4 import BeautifulSoup
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, "../../../"))

sys.path.append(project_dir)
from webScanV1.Config import C

def obtener_titulo(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            titulo = soup.title.text
            return titulo
        else:
            print(f"Error al realizar la solicitud. Código de estado: {response.status_code}")
            return None
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("<URL>")
    else:
        url = sys.argv[1]
        titulo_pagina = obtener_titulo(url)

        if titulo_pagina:
            print(f"{C.GN} Page title: {titulo_pagina}")
