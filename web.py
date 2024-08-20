# 09/03/2023 05:33 PM
# webScan v1.0.0 - securitySploit-Framework
#
# Copyright © 2024 Moicano
# Este proyecto está protegido por derechos de autor y se proporciona bajo la Licencia MIT.
# Más detalles en el archivo LICENSE.
#
# NOTA: El titular del copyright no es responsable de ningún mal uso
# que pueda ocurrir con esta herramienta. Úsala bajo tu propio riesgo.

import sys
import os
import urllib.request
import json
import gzip
import zlib
from urllib.request import urlopen
from io import BytesIO
import http.client
from urllib.parse import urlparse
from urllib.error import HTTPError, URLError
from html.parser import HTMLParser
from http.cookiejar import CookieJar
import datetime
import socket
import re
import ssl
import subprocess
import random

sys.dont_write_bytecode = True

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
from WebWeaver import WebWeaver
from Config import USER_AGENTS, puertos, C
os.environ["PYTHONDONTWRITEBYTECODE"] = "0"

class LinkParser(HTMLParser):
    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url

def load_routes_from_file(filename):
    try:
        with open(filename, "r") as file:
            routes = [line.strip() for line in file.readlines()]
        return routes
    except FileNotFoundError:
        print(f"{C.ERW} The file '{filename}' was not found")
        sys.exit(1)

def load_database_names(filename):
    try:
        with open(filename, "r") as file:
            database_names = [line.strip() for line in file.readlines()]
        return database_names
    except FileNotFoundError:
        print(f"{C.ERW} The file '{filename}' was not found")
        sys.exit(1)

def get_cookies(url):
    cookie_jar = http.cookiejar.CookieJar()
    
    selected_user_agent = random.choice(USER_AGENTS)
    headers = {
        'User-Agent': selected_user_agent,
        'Accept-Language': random.choice(['es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'en-US,en;q=0.9,es;q=0.8']),
        'Accept-Encoding': random.choice(['gzip, deflate, br', 'deflate, gzip, br']),
        'Referer': f'{url}',
    }

    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar), urllib.request.HTTPHandler())
    
    try:
        request = urllib.request.Request(url, headers=headers)
        with opener.open(request) as response:
            pass
    except urllib.error.URLError as e:
        if "-v" in sys.argv:
            print(f"Error connecting to the URL: {url} - Error: {e}")
        else:
            print(f"Error connecting to the URL: {url}")
        return None

    cookies = []
    for cookie in cookie_jar:
        httponly_flag = "HttpOnly" if "httponly" in cookie._rest.keys() else "no HttpOnly"
        print(f"{C.ALO} Cookie: {cookie.name} - {httponly_flag}")
        cookies.append(cookie.name)

def check_server_sistem(server_version):
    Sistem_filename = f"{C.dir_A}/SCRIPTS/TEXT/Sistem.txt"
    Sistem_printed = False

    try:
        with open(Sistem_filename, "r") as file:
            Sistem_data = [line.strip() for line in file.readlines()]

        for line in Sistem_data:
            System, System2 = line.split(" | ")
            if System2.lower() in server_version.lower():
                if not Sistem_printed:
                    print(f"{C.GN} System: {C.R}{C.G}{System}{C.T}")
                    Sistem_printed = True
                break

        if not Sistem_printed:
            pass

    except FileNotFoundError:
        print(f"{C.ERW} The file '{Sistem_data}' was not found")
        sys.exit()

def check_server_vulnerabilities(server_version):
    vulnerabilities_filename = f"{C.dir_A}/SCRIPTS/TEXT/vulnerabilidades.txt"
    vulnerability_printed = False

    try:
        with open(vulnerabilities_filename, "r") as file:
            vulnerabilities_data = [line.strip() for line in file.readlines()]

        for line in vulnerabilities_data:
            server_name, vulnerability = line.split(" : ")
            if server_name.lower() in server_version.lower():
                if not vulnerability_printed:
                    print(f"{C.GN} {server_version} {C.W}>{C.T} {C.R}{C.S}{C.I}{vulnerability}{C.T}")
                    vulnerability_printed = True
                break

        if not vulnerability_printed:
            print(f"{C.GN} Server: {server_version}")

    except FileNotFoundError:
        print(f"{C.ERW} The file '{vulnerabilities_filename}' was not found")
        sys.exit()

def check_server_info(url):
    try:
        response = urllib.request.urlopen(url)
        server_version = response.headers.get("Server", "Unknown")
        check_server_vulnerabilities(server_version)
        check_server_sistem(server_version)
        ssl_tls_info = get_ssl_tls_version(url)
        print(f"{ssl_tls_info}")
        analyze_technologies(url)

        print("---------------------------------------------------------")

        cookies = get_cookies(url)
        if cookies:
            for cookie in cookies:
                print(f"{C.ALO} Cookie: {cookie}")
        else:
            pass

        check_csrf_token(url)

        for puerto in puertos:
            verficar_puerto(url, puerto)

    except URLError as e:
        if "-v" in sys.argv:
            print(f"{C.ERW} Error connecting to the URL: {url} - Error: {e}")
            sys.exit(1)
        else:
            print(f"{C.ERW} Error connecting to the URL: {url}")
        sys.exit(1)
    except Exception as e:
        if "-v" in sys.argv:
            print(f"{C.ERW} Error retrieving server information: {e}")
        else:
            print(f"{C.ERW} Error retrieving server information")

def check_ssl_vulnerabilities(ssl_version):
    vulnerabilities_filename = f"{C.dir_A}/SCRIPTS/TEXT/ssl.txt"
    try:
        with open(vulnerabilities_filename, "r") as file:
            vulnerabilities_data = [line.strip() for line in file.readlines()]
        
        for line in vulnerabilities_data:
            version, vulnerability = line.split(" | ")
            if version.lower() in ssl_version.lower():
                return f"{C.W}>{C.T} {C.I}{C.R}{C.S}{vulnerability}{C.T}"

    except FileNotFoundError:
        return f"{C.ERW} El archivo '{vulnerabilities_filename}' no fue encontrado"
    
    return ""

def get_ssl_tls_version(url):
    try:
        parsed_url = urllib.parse.urlparse(url)
        hostname = parsed_url.hostname

        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                ssl_version = ssock.version()

                cert = ssock.getpeercert()
                expiration_date = cert.get('notAfter', 'Unknown')
                country_name = next((value for ((key, value),) in cert['issuer'] if key == 'countryName'), 'Unknown')
                organization_name = next((value for ((key, value),) in cert['issuer'] if key == 'organizationName'), 'Unknown')

                vulnerabilities_result = check_ssl_vulnerabilities(ssl_version)
                return f"{C.GN} SSL/TLS Enabled - Version: {ssl_version} - Expiration Date: {expiration_date} - Country: {country_name} - Organization: {organization_name} {vulnerabilities_result}"
    except (socket.error, ssl.SSLError) as e:
        return f"{C.GN} SSL/TLS Disabled"

def check_clickjacking(url):
    try:
        response = urllib.request.urlopen(url)
        headers = response.headers

        x_frame_options = headers.get("X-Frame-Options", "")
        if "DENY" in x_frame_options.upper() or "SAMEORIGIN" in x_frame_options.upper():
            pass
        else:
            print(f"{C.AL} Clickjacking: {url} - X-Frame-Options")

    except URLError as e:
        if "-v" in sys.argv:
            print(f"{C.ERW} Error connecting to the URL: {url} - Error: {e}")
            sys.exit(1)
        else:
            print(f"{C.ERW} Error connecting to the URL: {url}")
        sys.exit(1)
    except Exception as e:
        if "-v" in sys.argv:
            print(f"{C.ERW} Error retrieving server information: {e}")
        else:
            pass

def check_title(url):
    target_tags = ['title']
    options = {'title': {'content_only': True}}
    
    results = WebWeaver(url, target_tags, options, get_random_user_agent())
    
    if results:
        print(f"{C.GN} Page title: {results[0]}")
    else:
        subprocess.run(["python3", "-B", f"{C.dir_A}/SCRIPTS/INC/title.py", url])

def check_brute_force(url):
    subprocess.run(["python3", "-B", f"{C.dir_A}/SCRIPTS/forze.py", "-u", url])

def check_DoS(url):
    parsed_url = urlparse(url)

    NUM = "1000"
    URL = parsed_url.hostname
    puerto = parsed_url.port if parsed_url.port else 80
    path = parsed_url.path if parsed_url.path else '/'
    os.system(f"python3 -B {C.dir_A}/SCRIPTS/DoS_process.py {URL} {puerto} {path} {NUM} {url}")

def check_csrf_token(url):
    subprocess.run(["python3", "-B", f"{C.dir_A}/SCRIPTS/CSRF.py", url])

def check_csrf(url):
    subprocess.run(["python3", "-B", f"{C.dir_A}/SCRIPTS/CSRF_VULN.py", url])
    
def analyze_technologies(url):
    subprocess.run(["python3", "-B", f"{C.dir_A}/SCRIPTS/INC/anlizing_technologies.py", url])

def check_basic_robots_txt(url):
    subprocess.run(["python3", "-B", f"{C.dir_A}/SCRIPTS/robots.py", url])

def get_random_user_agent():
    return random.choice(USER_AGENTS)

def check_http_trace(url):
    try:
        parsed_url = urllib.parse.urlparse(url)
        hostname = parsed_url.hostname

        user_agent = get_random_user_agent()

        headers = {
            'User-Agent': user_agent
        }

        conn = http.client.HTTPConnection(hostname)
        conn.request("TRACE", "/", headers=headers)
        response = conn.getresponse()

        if response.status == 200:
            print(f"{C.AL} XST: {url} - HTTP TRACE enabled")
        else:
            pass

    except socket.gaierror as e:
        if "-v" in sys.argv:
            print(f"{C.ERW} Error resolving hostname: {e}")
        else:
            pass
    except Exception as e:
        if "-v" in sys.argv:
            print(f"{C.ERW} Error checking HTTP TRACE: {e}")
        else:
            pass

def check_databases(url, database_names):
    for name in database_names:
        full_url = urllib.parse.urljoin(url, name)
        try:
            response = urllib.request.urlopen(full_url)
            if response.status == 200:
                print(f"{C.GN} DB[{full_url}]")
        except HTTPError as e:
            if e.code != 404:
                print(f"{C.GN} DB Status:{e.code} {full_url}")

def server_vulnerabilities_port(server_version):
    dirA = os.path.dirname(__file__)
    vulnerabilities_filename = f"{dirA}/SCRIPTS/TEXT/vulnerabilidades_port.txt"
    
    try:
        with open(vulnerabilities_filename, "r") as file:
            vulnerabilities_data = [line.strip() for line in file.readlines()]
        
        for line in vulnerabilities_data:
            server_name, vulnerability = line.split(" | ")
            if server_name.lower() in server_version.lower():
                return f"{C.W}>{C.T} {C.R}{C.S}{C.I}{vulnerability}{C.T}"

    except FileNotFoundError:
        print(f"{C.ERW} The file '{vulnerabilities_filename}' was not found")
        sys.exit(1)
    
    return ""

def get_service_name(port):
    try:
        service_name = socket.getservbyport(port)
        return service_name
    except (socket.error, OSError):
        return "Unknown"

def is_compressed(data):
    try:
        zlib.decompress(data, -15)
        return True
    except zlib.error:
        return False

def get_service_version(ip, puerto):
    try:
        with socket.create_connection((ip, puerto), timeout=1) as sock:
            banner = sock.recv(1024)
            
            if is_compressed(banner):
                banner = zlib.decompress(banner, -15)

            try:
                decoded_banner = banner.decode("utf-8", errors="replace").strip()
                if not all(32 <= ord(char) <= 126 or char in ("\n", "\r", "\t") for char in decoded_banner):
                    return "Invalid characters"
                return decoded_banner
            except UnicodeDecodeError:
                try:
                    decoded_banner = banner.decode("latin-1", errors="replace").strip()
                    if not all(32 <= ord(char) <= 126 or char in ("\n", "\r", "\t") for char in decoded_banner):
                        return "Invalid characters"
                    return decoded_banner
                except UnicodeDecodeError:
                    return "Invalid characters"
    except (socket.error, ConnectionRefusedError, TimeoutError):
        return "Unknown"
    except Exception as e:
        if "-v" in sys.argv:
            print(f"Error getting service version for {ip}:{puerto}: {e}")
        return "Unknown"

def verficar_puerto(host, puerto):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        ip_match = re.search(r'\d+\.\d+\.\d+\.\d+', host)
        if ip_match:
            ip = ip_match.group()
        else:
            parsed_url = urllib.parse.urlparse(host)
            ip = socket.gethostbyname(parsed_url.hostname)

        resultado = sock.connect_ex((ip, puerto))

        if resultado == 0:
            service_name = get_service_name(puerto)
            try:
                service_version = get_service_version(ip, puerto)
                vulnerability = server_vulnerabilities_port(service_version)
                print(f"{C.ALO} Port: {puerto:<4} open - Service: {service_name:<15} - Version: {service_version} {vulnerability}")
            except UnicodeDecodeError:
                print(f"{C.ALO} Port: {puerto:<4} open - Service: {service_name:<15} - Version: Error decoding banner (UnicodeDecodeError)")
            except Exception as e:
                print(f"{C.ALO} Port: {puerto:<4} open - Service: {service_name:<15} - Version: Error decoding banner ({type(e).__name__})")
        else:
            pass

        sock.close()
    except Exception as e:
        if "-v" in sys.argv:
            print(f"{C.ERW} Error verifying the port {puerto}: {e}")
        else:
            pass

def obtener_ubicacion_ip(ip):
    try:
        url = f"http://ipinfo.io/{ip}/json"
        respuesta = urlopen(url)
        
        if respuesta.info().get("Content-Encoding") == "gzip":
            datos = gzip.GzipFile(fileobj=BytesIO(respuesta.read())).read()
        else:
            datos = respuesta.read()

        datos_decodificados = datos.decode("utf-8")
        datos_json = json.loads(datos_decodificados)

        ciudad = datos_json.get("city", "")
        region = datos_json.get("region", "")
        pais = datos_json.get("country", "")

        elementos_no_vacios = [elemento for elemento in [ciudad, region, pais] if elemento]

        ubicacion = ", ".join(elementos_no_vacios)

        return f"{C.GN} Possible Location: {ubicacion}" if ubicacion else None
    except Exception as e:
        if "-v" in sys.argv:
            return f"Error: {str(e)}"
        else:
            pass

def main():
    try:
        if len(sys.argv) < 3 or sys.argv[1] != "-u":
            print("Usage: web -u <URL> [-v]")
            sys.exit(1)

        url = sys.argv[2]

        selected_user_agent = random.choice(USER_AGENTS)
        
        parsed_url = urlparse(url)
        HostHeader = parsed_url.hostname
        headers = {
'Connection': 'keep-alive',
'User-Agent': selected_user_agent,
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'Accept-Encoding': random.choice(['gzip, deflate, br', 'deflate, gzip, br']),
'Accept-Language': random.choice(['es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6']),
'Cookie': 'p2n9185icbjbfe4r1h8gg3fnsl; PHPSSID=p2n9185icbjbfe4r1h8gg3fnsl',
'Referer': f'{url}',
    }

        opener = urllib.request.build_opener()
        opener.addheaders = [(key, value) for key, value in headers.items()]
        urllib.request.install_opener(opener)

        ip_match = re.search(r'\d+\.\d+\.\d+\.\d+', url)
        if ip_match:
            host_ip = ip_match.group()
        else:
            parsed_url = urllib.parse.urlparse(url)
            host_ip = socket.gethostbyname(parsed_url.hostname)

        print("webScan (sSf) v1.0.0")
        print("---------------------------------------------------------")
        now = datetime.datetime.now()
        hora_actual = now.strftime("%Y-%m-%d %I:%M:%p")
        print(f"{C.GN} Start time {hora_actual} (GMT)")
        print(f"{C.GN} Target: {url}")
        print(f"{C.GN} IP target: {host_ip}")
        check_title(url)
        resultado = obtener_ubicacion_ip(host_ip)
        if resultado is not None:
            print(resultado)
        check_server_info(url)
        check_clickjacking(url)
        check_http_trace(url)
        check_csrf(url)
        #check_brute_force(url)
        #check_DoS(url)
        #check_basic_robots_txt(url)
        print("---------------------------------------------------------")

        routes_filename = f"{C.dir_A}/SCRIPTS/TEXT/rutas.txt"
        databases_filename = f"{C.dir_A}/SCRIPTS/TEXT/data_base.txt"

        routes = load_routes_from_file(routes_filename)
        database_names = load_database_names(databases_filename)

        print

        error_403_count = 0
        error_403_printed = False

        for route in routes:
            full_url = urllib.parse.urljoin(url, route)
            try:
                response = urllib.request.urlopen(full_url)
                if response.status == 200:
                    print(f"{C.GN} Dir[{full_url}]")
            except HTTPError as e:
                if e.code != 404:
                    print(f"{C.GN} Dir Status[{e.code}]: {full_url}")
                    if e.code == 403: 
                        error_403_count += 1
                        if error_403_count >= 20 and not error_403_printed:
                            print(f"{C.I}{C.R}{C.S}20 or more 403 errors detected. The error may be due to server configuration. The scanning will be stopped.{C.T}")
                            error_403_printed = True
                            exit()
            except Exception as e:
                if "-v" in sys.argv:
                    print(f"{C.ERW} Error accessing the URL: {full_url} - Error: {e}")
                else:
                    pass

        try:
            with urllib.request.urlopen(url) as response:
                html_data = response.read()
                parser = LinkParser(url)
                parser.feed(html_data.decode("utf-8"))
        except Exception as e:
            if "-v" in sys.argv:
                print(f"{C.ERW} Error parsing the source code: {e}")
            else:
                pass

        check_databases(url, database_names)

        now = datetime.datetime.now()
        hora_actual = now.strftime("%Y-%m-%d %I:%M:%p")
        print("---------------------------------------------------------")
        print(f"{C.GN} End time {hora_actual} (GMT)")

    except KeyboardInterrupt:
        now = datetime.datetime.now()
        hora_actual = now.strftime("%Y-%m-%d %I:%M:%p")
        print("---------------------------------------------------------")
        print(f"{C.GN} End time {hora_actual} (GMT)")
        print()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        if "-v" in sys.argv:
            print(f"{C.ERW} {e}")
        else:
            pass
