import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent


class Interfax:

    @staticmethod
    def get_news():
        response = requests.get('https://www.interfax.ru/',
                                headers={'User-Agent': generate_user_agent(device_type='desktop',
                                                                                         os=('mac', 'linux'))})
        soup = BeautifulSoup(response.content, 'html.parser')

        all_news = []
        all_news.append(soup.select("div[class='timeline__text'] a"))
        all_news.append(soup.select("div[class='timeline__group'] a"))
        all_news.append(soup.select("div[class='timeline__photo'] a"))

        news_list = []
        for news in all_news:
            for i in news:
                if i.get_text() != '':
                    news = {'name': 'interfax.ru',
                            'title': i.getText(),
                            'link': 'https://interfax.ru' + i['href']}
                    news_list.append(news)

        return news_list
