import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent
from abc import ABC, abstractmethod


class BaseNews(ABC):

    def parse(self):
        name = self.get_name()
        url = self.get_url()
        selectors = self.get_selectors()

        response = requests.get(url,
                                headers={'User-Agent': generate_user_agent(device_type='desktop',
                                                                           os=('mac', 'linux'))})

        soup = BeautifulSoup(response.content, 'html.parser')

        news_list = []

        for sel in selectors:
            news = soup.select(sel)

            for i in news:
                if self.get_link(i):
                    if i.get_text() != '':
                        link = self.get_link(i)

                        news = {'name': name,
                                'title': i.get_text(),
                                'link': link}

                        if news not in news_list:
                            news_list.append(news)

        return news_list

    @abstractmethod
    def get_url(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_selectors(self):
        pass

    @abstractmethod
    def get_link(self, news):
        pass
