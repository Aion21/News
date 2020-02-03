import re
from app.core.base_news import BaseNews
from app.core.selectors import bbc_selectors


class BBC(BaseNews):

    def parse(self):
        return super().parse()

    def get_url(self):
        return 'https://www.bbc.com/news'

    def get_name(self):
        return 'bbc.com'

    def get_selectors(self):
        return bbc_selectors

    def get_link(self, news):
        return 'https://www.bbc.com' + news.parent['href'] \
            if news.parent['href'] != re.compile('^https') \
            else news.parent['href']
