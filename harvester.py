from lxml import html
from scraper import Scraper


class Harvester:

    def __init__(self, web_page):
        self.url = Scraper(web_page)

    def get_quote(self):
        tree = self.get_tree_page()
        quote = tree.xpath('(//div[@id="mw-content-text"]//ul//li)[1]/text()')
        return quote[0]

    def get_tree_page(self):
        page = self.url.download_page()
        tree = html.fromstring(page.content)
        return tree

