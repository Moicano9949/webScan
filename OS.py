import re
from bs4 import BeautifulSoup
import requests
from Colores import C

def obtener_plataforma_correo(dominio):
    plataformas = {
        "gmail.com": "Google",
        "outlook.com": "Microsoft",
        "hotmail.com": "Microsoft",
        "yahoo.com": "Yahoo",
        ".edu": "education",
    }

    for patron, plataforma in plataformas.items():
        if re.search(patron, dominio):
            return plataforma
    return 'Desconocido'

def escanear_sitio(url):
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    correos_electronicos = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', soup.get_text())

    patrones_enlaces_sociales = ["facebook.com", "twitter.com", "instagram.com", "tiktok.com", "whatsapp.com", "linkedin.com", "snapchat.com", "pinterest.com", "reddit.com", "tumblr.com", "discord.com", "gitlab.com", "infosec.exchange", "quora.com", "youtube.com", "skype.com", "viber.com", "flickr.com", "wechat.com", "line.me", "medium.com", "telegram.org", "github.com", "soundcloud.com", "deviantart.com", "meetup.com", "twitch.tv", "dribbble.com", "slack.com"]
    enlaces_sociales = set()

    for etiqueta_a in soup.find_all("a", href=True):
        for patron in patrones_enlaces_sociales:
            if patron in etiqueta_a["href"]:
                enlaces_sociales.add(etiqueta_a["href"])

    if correos_electronicos:
        print(f"{C.GN} Email(s):")
        for correo in correos_electronicos:
            dominio = correo.split("@")[-1]
            plataforma = obtener_plataforma_correo(dominio)
            print(f"- {correo} - {plataforma}")
    else:
        print

    if enlaces_sociales:
        print(f"\n{C.GN} Social Link(s):")
        for enlace in enlaces_sociales:
            print(f"- {enlace}")
    else:
        print

url_ejemplo = "https://www.kali.org/tools/"
escanear_sitio(url_ejemplo)
