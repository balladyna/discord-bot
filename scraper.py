import logging
import os
import requests

logging.basicConfig(filemode='errors.log', level=logging.ERROR, format='%(levelname)s:%(message)s')


class Scraper:

    def __init__(self, web_url):
        self.url = web_url

    def download_page(self):
        try:
            with open(self._create_file_path(), 'wb+') as web_page:
                html = requests.get(self.url)
                html_file = web_page.write(html.content)
                return html
        except (ValueError, AttributeError, EOFError, OverflowError, FileNotFoundError) as error:
            logging.error('Downloading page', error)

    def _create_file_path(self):
        try:
            file_name = '/website_content'
            return ''.join([self._create_directory(), file_name])
        except FileExistsError as error:
            logging.error('Saving file', error)

    def _create_directory(self):
        try:
            parent_directory = os.getcwd()
            web_directory = 'web_data'
            path = os.path.join(parent_directory, web_directory)
            if not self._is_directory_exist(path):
                os.mkdir(path)
            return path
        except FileExistsError as error:
            logging.error('Create directory', error)

    @staticmethod
    def _is_directory_exist(directory_path):
        return os.path.exists(directory_path)
