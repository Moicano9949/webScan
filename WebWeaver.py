import urllib.request
from html.parser import HTMLParser
import gzip
from io import BytesIO
import random
from Config import USER_AGENTS

class MyHTMLParser(HTMLParser):
    def __init__(self, target_tags=None, options=None):
        super().__init__()
        self.target_tags = target_tags
        self.options = options
        self.current_tag = None
        self.in_target_tag = False
        self.results = []

    def handle_starttag(self, tag, attrs):
        if tag in self.target_tags:
            self.current_tag = tag
            self.in_target_tag = True

            if self.options and tag in self.options:
                option = self.options[tag]
                if 'content_only' in option and option['content_only']:
                    self.results.append('')
                elif 'full_tag' in option and option['full_tag']:
                    self.results.append(self.get_starttag_text())

    def handle_endtag(self, tag):
        if self.in_target_tag and tag == self.current_tag:
            self.in_target_tag = False
            self.current_tag = None

    def handle_data(self, data):
        if self.in_target_tag:
            if self.options and self.current_tag in self.options:
                option = self.options[self.current_tag]
                if 'content_only' in option and option['content_only']:
                    self.results[-1] += data.strip()

def get_random_user_agent():
    return random.choice(USER_AGENTS)

def WebWeaver(url, target_tags=None, options=None, user_agent=None):
    try:
        user_agent = user_agent or get_random_user_agent()
        headers = {'Accept-Encoding': 'gzip', 'User-Agent': user_agent}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            if response.headers.get('Content-Encoding') == 'gzip':
                compressed_data = response.read()

                with gzip.GzipFile(fileobj=BytesIO(compressed_data), mode='rb') as f:
                    data = f.read()
            else:
                data = response.read()

        decoded_data = data.decode(response.headers.get_content_charset('utf-8') or 'latin-1', 'ignore')

        if target_tags:
            parser = MyHTMLParser(target_tags, options)
            parser.feed(decoded_data)

            return parser.results

        return decoded_data

    except urllib.error.URLError as e:
        print(f"Error al realizar la solicitud: {e}")
    except Exception as e:
        print(f"Error: {e}")
        return None
