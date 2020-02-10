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
        if news.parent.get('href'):
            return 'https://www.bbc.com' + news.parent['href'] \
                if not re.match('^https', news.parent['href']) \
                else news.parent['href']
        else:
            return None
