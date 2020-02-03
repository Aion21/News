from app.core.base_news import BaseNews
from app.core.selectors import interfax_selectors


class Interfax(BaseNews):

    def parse(self):
        return super().parse()

    def get_url(self):
        return 'https://www.interfax.ru'

    def get_name(self):
        return 'interfax.ru'

    def get_selectors(self):
        return interfax_selectors

    def get_link(self, news):
        return self.get_url() + news['href']
