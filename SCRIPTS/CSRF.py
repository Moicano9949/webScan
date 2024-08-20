import requests
from bs4 import BeautifulSoup
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, "../../"))

sys.path.append(project_dir)
from webScanV1.Config import C

if len(sys.argv) != 2:
    print("<URL>")
    sys.exit(1)

url = sys.argv[1]

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
headers = {"User-Agent": user_agent}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    csrf_token_input = soup.find("input", {"name": lambda name: name and "csrf" in name.lower()})

    if csrf_token_input:
        print(f"{C.ALO} Token CSRF: {C.G}{csrf_token_input['value']}{C.T}")
    else:
        print

    keyword_csrf = soup.find(string=lambda text: "csrf" in str(text).lower())
    if keyword_csrf:
        print(f"{C.ALO} Keyword 'CSRF' found: {C.Y}{keyword_csrf}{C.G}")
else:
    print(f"{C.ERW} Error requesting page. Status code: {response.status_code}")
