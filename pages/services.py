from html.parser import HTMLParser
import requests


class PageParser(HTMLParser):
    """
    Парсинг HTML-документа для подсчета количества заголовков и извлечения ссылок
    """

    def __init__(self):
        super().__init__()
        self.title = 0
        self.subtitle = 0
        self.content = 0
        self.links = []

    def counter(self, tag, attrs):
        if tag == "h1":
            self.title += 1
        elif tag == "h2":
            self.subtitle += 1
        elif tag == "h3":
            self.content += 1
        elif tag == "a":
            for attr in attrs:
                if attr[0] == "href":
                    self.links.append(attr[1])


def parse_page(url):
    """ "
    Метод для парсинга страницы по URL
    """

    response = requests.get(url)
    parser = PageParser()
    parser.feed(response.text)
    return parser.title, parser.subtitle, parser.content, parser.links
