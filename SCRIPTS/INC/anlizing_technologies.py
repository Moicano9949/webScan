import http.client
import urllib.request
from bs4 import BeautifulSoup
import re
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, "../../../"))

sys.path.append(project_dir)
from webScanV1.Config import C

class TechnologyParser:
    def __init__(self, pattern_file):
        self.technologies = set()
        self.load_patterns(pattern_file)

    def load_patterns(self, pattern_file):
        try:
            with open(pattern_file, "r") as file:
                self.technology_patterns = [line.strip() for line in file.readlines()]
        except FileNotFoundError as e:
            print(f"{C.ERW} Error loading patterns: {e}")
            sys.exit(1)

    def extract_technologies_from_url(self, url):
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
            req = urllib.request.Request(url, headers=headers)

            with urllib.request.urlopen(req) as response:
                html_data = response.read()

            soup = BeautifulSoup(html_data, 'html.parser')

            for tag in soup.find_all(['script', 'link']):
                if tag.get('src') or tag.get('href'):
                    url_value = tag.get('src') or tag.get('href')
                    self.extract_technology_from_url(url_value)

            x_powered_by = response.getheader("X-Powered-By")
            if x_powered_by:
                print(f"{C.GN} {x_powered_by} - X-Powered-By")

        except Exception as e:
            print(f"{C.ERW} Error analyzing technologies: {e}")
            sys.exit(1)

    def extract_technology_from_url(self, url):
        for pattern_line in self.technology_patterns:
            technology, pattern = pattern_line.split(" : ")
            if re.search(pattern, url, re.IGNORECASE):
                self.technologies.add(technology)
                break

    def get_technologies(self):
        return list(self.technologies)

def analyze_technologies(url, verbose=False):
    pattern_file = f"{C.dir_A}/SCRIPTS/TEXT/use_tecnologias.txt"
    parser = TechnologyParser(pattern_file)

    try:
        parser.extract_technologies_from_url(url)
        technologies_used = parser.get_technologies()

        if technologies_used:
            print(f"{C.GN} Possible technologies used:")
            for technology in technologies_used:
                print(f" - {technology}")
        else:
            print

    except Exception as e:
        if verbose:
            print(f"{C.ERW} Error analyzing technologies: {e}")
        else:
            print(f"{C.ERW} Error analyzing technologies. Use -v for more details.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3 or (len(sys.argv) == 3 and sys.argv[1] != '-v'):
        print("Usage: python script.py [-v] <url>")
        sys.exit(1)

    url = sys.argv[-1]
    verbose = '-v' in sys.argv
    analyze_technologies(url, verbose)
