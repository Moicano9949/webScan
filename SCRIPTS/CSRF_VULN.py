import requests
from bs4 import BeautifulSoup
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, "../../"))

sys.path.append(project_dir)
from webScanV1.Config import C

def comparacion(url):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

    headers = {"User-Agent": user_agent}
    response1 = requests.get(url, headers=headers)
    data1 = response1.text

    soup = BeautifulSoup(data1, "html.parser")
    input_fields = soup.find_all("input")

    if input_fields:
        print

        response2 = requests.get(url, headers=headers)
        data2 = response2.text

        if data1 == data2:
            print(f"{C.AL} CSRF: {url}")
        else:
            print

    else:
        print

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("<url>")
        sys.exit(1)

    url = sys.argv[1]
    comparacion(url)
