import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent


class Ria:

    @staticmethod
    def get_news():
        response = requests.get('https://ria.ru',
                                headers={'User-Agent': generate_user_agent(device_type='desktop',
                                                                           os=('mac', 'linux'))})

        soup = BeautifulSoup(response.content, 'html.parser')

        all_news = []
        all_news.append(soup.select('span.cell-list__item-title'))
        all_news.append(soup.select('span.cell-main-photo__title'))

        news_list = []

        for news in all_news:
            for i in news:
                if i.getText() != ' ':
                    news = {'name': 'ria.ru',
                            'title': i.getText(),
                            'link': i.parent.parent['href']}
                    news_list.append(news)

        return news_list
