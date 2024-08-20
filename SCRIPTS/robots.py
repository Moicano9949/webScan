import urllib.request
from urllib.parse import urljoin
import random
import sys

def obtener_robots_txt(url, user_agent):
    robots_url = urljoin(url, "/robots.txt")
    try:
        headers = {'User-Agent': user_agent}
        request = urllib.request.Request(robots_url, headers=headers)
        with urllib.request.urlopen(request) as response:
            return response.read().decode("utf-8")
    except (urllib.error.HTTPError, urllib.error.URLError) as e:
        return None

def analizar_robots_txt(robots_content, user_agent):
    rutas_importantes = [
        "/admin/",
        "/private/",
        "/cgi-bin/",
        "/secret/",
        "/confidential/",
        "/hidden/",
        "/backup/",
        "/logs/",
        "/database/",
        "/config/",
        "/config.php",
        "/wp-admin/",
        "/wp-login.php",
        "/phpmyadmin/",
        "/sitemap.xml",
        "/cgi-bin/",
        "/admin/",
        "/private/",
        "/secret/",
        "/confidential/",
        "/hidden/",
        "/backup/",
        "/logs/",
        "/database/",
        "/config/",
        "/config.php",
        "/wp-admin/",
        "/wp-login.php",
        "/phpmyadmin/",
    ]

    if robots_content:
        for line in robots_content.split("\n"):
            line = line.strip()
            if line and not line.startswith("#"):
                if line.lower().startswith("user-agent:"):
                    user_agent = line.split(":", 1)[1].strip()
                elif line.lower().startswith(("disallow:", "allow:")):
                    directive, value = map(str.strip, line.split(":", 1))
                    if value in rutas_importantes:
                        print(f"{user_agent}: {directive.capitalize()}: {value}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <URL>")
    else:
        sitio_web = sys.argv[1]
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
        ]

        for user_agent in user_agents:
            contenido_robots = obtener_robots_txt(sitio_web, user_agent)
            if contenido_robots is not None:
                analizar_robots_txt(contenido_robots, user_agent)
