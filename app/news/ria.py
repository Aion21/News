from app.core.base_news import BaseNews
from app.core.selectors import ria_selectors


class Ria(BaseNews):

    def parse(self):
        return super().parse()

    def get_url(self):
        return 'https://ria.ru'

    def get_name(self):
        return 'ria.ru'

    def get_selectors(self):
        return ria_selectors

    def get_link(self, news):
        return news.parent.parent['href']
