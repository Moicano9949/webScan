import http.cookiejar
import urllib.request
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, "../../"))

sys.path.append(project_dir)
from WEB.Config import C

def extract_csrf_token(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        csrf_tokens = soup.find_all('input', {'name': lambda x: x and 'csrf' in x.lower()} ) + soup.find_all('input', {'id': lambda x: x and 'csrf' in x.lower()})
        for token in csrf_tokens:
            if token and token.get('value'):
                return token.get('value')
    except Exception as e:
        print(f"Error al extraer token CSRF: {e}")

    return None

def main():
    try:
        if len(sys.argv) < 13 or sys.argv[1] != "-u" or sys.argv[3] != "-p" or sys.argv[5] != "-b" or sys.argv[7] != "-url" or sys.argv[9] != "-Iu" or sys.argv[11] != "-Ip" or sys.argv[13] not in ["-M", "GET", "POST"]:
            print(f"Usage: python3 {sys.argv[0]} -u <username> -p <password> -b <button_name> -url <url> -Iu <usernombre_input> -Ip <passcontraseña_input> -M <method>")
            sys.exit(1)

        usuario = sys.argv[2]
        contraseña = sys.argv[4]
        nombre_boton = sys.argv[6]
        url = sys.argv[8]
        usernombre_input = sys.argv[10]
        passcontraseña_input = sys.argv[12]
        method = sys.argv[13]

        cookie_jar = http.cookiejar.CookieJar()

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))
        opener.addheaders = [('User-Agent', headers['User-Agent'])]
        urllib.request.install_opener(opener)

        payload = {
            f"{usernombre_input}": usuario,
            f"{passcontraseña_input}": contraseña,
            f"{nombre_boton}": nombre_boton
        }

        if method == "GET":
            url += f"?{urlencode(payload)}"
            request = urllib.request.Request(url)
        elif method == "POST":
            data = urlencode(payload).encode('utf-8')
            request = urllib.request.Request(url, data=data)

        request.add_header('User-Agent', headers['User-Agent'])
        response = opener.open(request)
        html_response = response.read().decode('utf-8')

        csrf_token = extract_csrf_token(html_response)

        if csrf_token:
            payload['csrf_token'] = csrf_token

        if method == "GET":
            url += f"?{urlencode(payload)}"
            request = urllib.request.Request(url)
        elif method == "POST":
            data = urlencode(payload).encode('utf-8')
            request = urllib.request.Request(url, data=data)

        request.add_header('User-Agent', headers['User-Agent'])
        response = opener.open(request)

        if "Home" in response.read().decode('utf-8'):
            print

            print
            for cookie in cookie_jar:
                http_only = "si" if cookie.has_nonstandard_attr("HttpOnly") else "no"
                print

            cookie_jar.clear_session_cookies()
            print

            request = urllib.request.Request(url)
            request.add_header('User-Agent', headers['User-Agent'])
            response_hijack = opener.open(request)

            if "Home" in response_hijack.read().decode('utf-8'):
                print(f"{C.AL} Cookie Hijacking")
            else:
                print
        else:
            print
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
