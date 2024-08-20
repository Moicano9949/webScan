#03/09/2023 05:33 PM
#webScan v1.0.0 - securitySploit-Framework
import sys
import os
import urllib.request
import http.client
from urllib.error import HTTPError, URLError
from html.parser import HTMLParser
from http.cookiejar import CookieJar
import datetime
import socket
import re
import ssl
import subprocess

R = "\033[31m"  # Rojo
G = "\033[32m"  # Verde
C = "\033[36m"  # Azul Cielo
W = "\033[97m"  # Blanco
Y = "\033[33m"  # Amarillo
A = "\033[34m"  # Azul
S = "\033[1m"   # Brillante
T = "\033[0m"   # RESET
I = "\033[7m"   # Invertido

dir_A = os.path.dirname(__file__)

AL = f"{R}{S}[{T}{Y}{S}!{T}{R}{S}]{T}"
ALO = f"{A}{S}[{T}{G}{S}+{T}{A}{S}]{T}"
GN = f"{W}{S}[{T}{W}+{T}{W}{S}]{T}"
ERW = f"{W}{S}[{T}{R}{S}-{T}{W}{S}]{T}"
LP = f"{C}═══════════════════════════════════{T}"
CO = "====================="
L = f"{A}=========================================={T}"

class LinkParser(HTMLParser):
    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url

class TechnologyParser(HTMLParser):
    def __init__(self, pattern_file):
        super().__init__()
        self.technologies = set()
        self.load_patterns(pattern_file)

    def load_patterns(self, pattern_file):
        try:
            with open(pattern_file, "r") as file:
                self.technology_patterns = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print(f"{ERW} The file '{pattern_file}' was not found")
            sys.exit(1)

    def handle_starttag(self, tag, attrs):
        if tag == "script":
            for attr, value in attrs:
                if attr == "src":
                    self.extract_technology_from_url(value)
        elif tag == "link":
            for attr, value in attrs:
                if attr == "href":
                    self.extract_technology_from_url(value)

    def extract_technology_from_url(self, url):
        for pattern_line in self.technology_patterns:
            technology, pattern = pattern_line.split(" : ")
            if re.search(pattern, url, re.IGNORECASE):
                self.technologies.add(technology)
                break

    def get_technologies(self):
        return list(self.technologies)

def analyze_technologies(url):
    try:
        response = urllib.request.urlopen(url)
        html_data = response.read()
        diRa = os.path.dirname(__file__)
        pattern_file = f"{diRa}/use_tecnologias.txt"
        parser = TechnologyParser(pattern_file)
        parser.feed(html_data.decode("utf-8"))
        technologies_used = parser.get_technologies()

        if technologies_used:
            print(f"{GN} Possible technologies used:")
            for technology in technologies_used:
                print(f" - {technology}")
        else:
            print

    except Exception as e:
        print(f"Error analyzing technologies: {e}")

def load_routes_from_file(filename):
    try:
        with open(filename, "r") as file:
            routes = [line.strip() for line in file.readlines()]
        return routes
    except FileNotFoundError:
        print(f"{ERW} The file '{filename}' was not found")
        sys.exit(1)

def load_database_names(filename):
    try:
        with open(filename, "r") as file:
            database_names = [line.strip() for line in file.readlines()]
        return database_names
    except FileNotFoundError:
        print(f"{ERW} The file '{filename}' was not found")
        sys.exit(1)

def get_cookies(url):
    cookie_jar = CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))
    
    try:
        with opener.open(url) as response:
            pass
    except URLError as e:
        print(f"{ERW} Error connecting to the URL.: {url} - Error: {e}")
        sys.exit(1)
    
    cookies = []
    for cookie in cookie_jar:
        httponly_flag = "HttpOnly" if "httponly" in cookie._rest.keys() else "Not HttpOnly"
        print(f"{ALO} Cookie: {cookie.name} - {httponly_flag}")
        cookies.append(cookie.name)

def check_server_vulnerabilities(server_version):
    dirA = os.path.dirname(__file__)
    vulnerabilities_filename = f"{dirA}/vulnerabilidades.txt"
    vulnerability_printed = False

    try:
        with open(vulnerabilities_filename, "r") as file:
            vulnerabilities_data = [line.strip() for line in file.readlines()]
        
        for line in vulnerabilities_data:
            server_name, vulnerability = line.split(" : ")
            if server_name.lower() in server_version.lower():
                if not vulnerability_printed:
                    print(f"{GN} {server_version} {W}>{T} {R}{S}{I}{vulnerability}{T}")
                    vulnerability_printed = True
                break

        if not vulnerability_printed:
            print(f"{GN} {server_version}")

    except FileNotFoundError:
        print(f"{ERW} The file '{vulnerabilities_filename}' was not found")
        sys.exit(1)

def check_server_info(url):
    try:
        response = urllib.request.urlopen(url)
        now = datetime.datetime.now()
        hora_actual = now.strftime("%Y-%m-%d %I:%M:%p")
        print(f"{GN} Start time {hora_actual} (GMT)")
        response = urllib.request.urlopen(url)
        server_version = response.headers.get("Server", "Desconocido")
        check_server_vulnerabilities(server_version)
        ssl_tls_info = get_ssl_tls_version(url)
        print(f"{ssl_tls_info}")
        analyze_technologies(url)

        print("---------------------------------------------------------")
        cookies = get_cookies(url)
        if cookies:
            for cookie in cookies:
                print(f"{ALO} Cookie: {cookie}")
        else:
            print
            
        puertos = [20, 21, 22, 3306, 23, 80, 25, 5432, 139, 445, 111, 5900, 1521, 1433, 27017, 6379, 9042, 50000, 8091, 11210, 513, 443, 990, 465, 110, 995, 143, 993, 8009, 8080, 1025, 2049, 2000, 3260, 69, 161, 68, 123, 137, 138, 162, 512, 514, 873, 2048, 3305, 5433, 8081, 8443, 9080, 9081, 50070, 50075, 50030, 50060, 2222, 8022, 8888, 9090, 8008, 10000, 54321, 20031, 6660, 6661, 6662, 6663, 6664, 6665, 6666, 6667, 6668, 6669, 6670, 11211, 9092, 9093, 9094, 9095, 9096, 9097, 9098, 9099,]

        for puerto in puertos:
            verficar_puerto(url, puerto)

    except URLError as e:
        print(f"{ERW} Error connecting to the URL: {url} - Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"{ERW} Error retrieving server information: {e}")

def check_ssl_vulnerabilities(ssl_version):
    vulnerabilities_filename = f"{dir_A}/ssl.txt"
    try:
        with open(vulnerabilities_filename, "r") as file:
            vulnerabilities_data = [line.strip() for line in file.readlines()]
        
        for line in vulnerabilities_data:
            version, vulnerability = line.split(" | ")
            if version.lower() in ssl_version.lower():
                return f"{W}>{T} {I}{R}{S}{vulnerability}{T}"

    except FileNotFoundError:
        return f"{ERW} El archivo '{vulnerabilities_filename}' no fue encontrado"
    
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
                return f"{GN} SSL/TLS Enabled - Version: {ssl_version} - Expiration Date: {expiration_date} - Country: {country_name} - Organization: {organization_name} {vulnerabilities_result}"
    except (socket.error, ssl.SSLError) as e:
        return f"{GN} SSL/TLS Disabled"

def check_clickjacking(url):
    try:
        response = urllib.request.urlopen(url)
        headers = response.headers

        x_frame_options = headers.get("X-Frame-Options", "")
        if "DENY" in x_frame_options.upper() or "SAMEORIGIN" in x_frame_options.upper():
            print
        else:
            print(f"{AL} Clickjacking: {url}")

    except URLError as e:
        print(f"{ERW} Error connecting to the URL: {url} - Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"{ERW} Error retrieving server information: {e}")
        

def check_brute_force(url):
    subprocess.run(["python3", f"{dir_A}/forze.py", "-u", url])
    
def check_brute_force_from_file(url, dirs_file):
    with open(dirs_file, 'r') as file:
        dirs_list = file.read().splitlines()

    for directory in dirs_list:
        full_url = f"{url}/{directory}"
        try:
            result = subprocess.run(["python3", f"{dir_A}/forze.py", "-u", full_url], capture_output=True, text=True)
            if "brute force" in result.stdout:
                print(result.stdout)
        except subprocess.CalledProcessError as e:
            pass


def check_http_trace(url):
    try:
        parsed_url = urllib.parse.urlparse(url)
        hostname = parsed_url.hostname

        conn = http.client.HTTPConnection(hostname)
        conn.request("TRACE", "/")
        response = conn.getresponse()

        if response.status == 200:
            print(f"{AL} XST: {url} - HTTP TRACE enabled")
        else:
            print

    except socket.gaierror as e:
        print(f"{ERW} Error resolving hostname: {e}")
    except Exception as e:
        print(f"{ERW} Error checking HTTP TRACE: {e}")

def check_databases(url, database_names):
    for name in database_names:
        full_url = urllib.parse.urljoin(url, name)
        try:
            response = urllib.request.urlopen(full_url)
            if response.status == 200:
                print(f"{GN} DB[{full_url}]")
        except HTTPError as e:
            if e.code != 404:
                print(f"{GN} DB Status:{e.code} {full_url}")

def get_service_name(port):
    try:
        service_name = socket.getservbyport(port)
        return service_name
    except (socket.error, OSError):
        return "Unknown"

def server_vulnerabilities_port(server_version):
    dirA = os.path.dirname(__file__)
    vulnerabilities_filename = f"{dirA}/vulnerabilidades_port.txt"
    
    try:
        with open(vulnerabilities_filename, "r") as file:
            vulnerabilities_data = [line.strip() for line in file.readlines()]
        
        for line in vulnerabilities_data:
            server_name, vulnerability = line.split(" | ")
            if server_name.lower() in server_version.lower():
                return f"{W}>{T} {R}{S}{I}{vulnerability}{T}"

    except FileNotFoundError:
        print(f"{ERW} The file '{vulnerabilities_filename}' was not found")
        sys.exit(1)
    
    return ""

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
                print(f"{ALO} Port: {puerto:<4} open - Service: {service_name:<15} - Version: {service_version} {vulnerability}")
            except UnicodeDecodeError:
                print(f"{ALO} Port: {puerto:<4} open - Service: {service_name:<15} - Version: Error decoding banner (UnicodeDecodeError)")
            except Exception as e:
                print(f"{ALO} Port: {puerto:<4} open - Service: {service_name:<15} - Version: Error decoding banner ({type(e).__name__})")
        else:
            print

        sock.close()
    except Exception as e:
        print(f"{ERW} Error verifying the port {puerto}: {e}")


def get_service_version(ip, puerto):
    try:
        with socket.create_connection((ip, puerto), timeout=1) as sock:
            banner = sock.recv(1024)
            try:
                decoded_banner = banner.decode("utf-8", errors="replace").strip()
                if not all(32 <= ord(char) <= 126 or char in ("\n", "\r", "\t") for char in decoded_banner):
                    return "Invalid characters"
                return decoded_banner
            except UnicodeDecodeError:
                return "Invalid characters"
    except (socket.error, ConnectionRefusedError, TimeoutError):
        return "Unknown"
    except Exception as e:
        print(f"{ERW} Error getting service version for {ip}:{puerto}: {e}")
        return "Unknown"

def main():
    try:
        if len(sys.argv) != 3 or sys.argv[1] != "-u":
            print("Usage: web -u <URL>")
            sys.exit(1)

        url = sys.argv[2]
        
        ip_match = re.search(r'\d+\.\d+\.\d+\.\d+', url)
        if ip_match:
            host_ip = ip_match.group()
        else:
            parsed_url = urllib.parse.urlparse(url)
            host_ip = socket.gethostbyname(parsed_url.hostname)

        print("webScan (sSf) v1.0.0")
        print("---------------------------------------------------------")
        print(f"{GN} Target: {url}")
        print(f"{GN} IP target: {host_ip}")
        check_server_info(url)
        check_clickjacking(url)
        check_http_trace(url)
        check_brute_force(url)
        check_brute_force_from_file(url, f"{dir_A}/data_base.txt")
        print("---------------------------------------------------------")
        
        routes_filename = f"{dir_A}/rutas.txt"
        databases_filename = f"{dir_A}/data_base.txt"

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
                    print(f"{GN} Dir[{full_url}]")
            except HTTPError as e:
                if e.code != 404:
                    print(f"{GN} Dir Status[{e.code}]: {full_url}")
                    if e.code == 403: 
                        error_403_count += 1
                        if error_403_count >= 20 and not error_403_printed:
                            print(f"{I}{R}{S}20 or more 403 errors detected. The error may be due to server configuration. The scanning will be stopped.{T}")
                            error_403_printed = True
                            exit()
            except Exception as e:
                print(f"{ERW} Error accessing the URL: {full_url} - Error: {e}")

        try:
            with urllib.request.urlopen(url) as response:
                html_data = response.read()
                parser = LinkParser(url)
                parser.feed(html_data.decode("utf-8"))
        except Exception as e:
            print(f"{ERW} Error parsing the source code: {e}")

        check_databases(url, database_names)

        now = datetime.datetime.now()
        hora_actual = now.strftime("%Y-%m-%d %I:%M:%p")
        print("---------------------------------------------------------")
        print(f"{GN} End time {hora_actual} (GMT)")

    except KeyboardInterrupt:
        now = datetime.datetime.now()
        hora_actual = now.strftime("%Y-%m-%d %I:%M:%p")
        print("---------------------------------------------------------")
        print(f"{GN} End time {hora_actual} (GMT)")
        print()

if __name__ == "__main__":
    main()