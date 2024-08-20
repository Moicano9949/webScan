import urllib.request
import urllib.error
import time
import sys
import os
import random

current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, "../../"))

sys.path.append(project_dir)
from WEB.Config import C, USER_AGENTS

def verificar_conexion(url, user_agent):
    try:
        request = urllib.request.Request(url, headers={'User-Agent': user_agent})
        with urllib.request.urlopen(request, timeout=5) as response:
            pass
    except urllib.error.HTTPError as e:
        print(f"{C.AL} DoS: {url} HTTP Error: {e.code}")
    except urllib.error.URLError as e:
        print(f"{C.AL} DoS: {url} URL Error: {e.reason}")
    except Exception as e:
        print(f"{C.AL} DoS: {url} Error desconocido: {e}")

if len(sys.argv) != 2:
    print("<URL>")
    sys.exit(1)

url_a_verificar = sys.argv[1]

user_agent = random.choice(USER_AGENTS)

time.sleep(3)
verificar_conexion(url_a_verificar, user_agent)