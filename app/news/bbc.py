import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent
import re


class BBC:

    @staticmethod
    def get_news():
        response = requests.get('https://www.bbc.com/news',
                                headers={'User-Agent': generate_user_agent(device_type='desktop',
                                                                           os=('mac', 'linux'))})

        soup = BeautifulSoup(response.content, 'html.parser')
        news = soup.select("h3[class^='gs-c-promo-heading__title']")

        news_list = []

        for i in news:
            news = {'name': 'bbc.com',
                    'title': i.get_text(),
                    'link': 'https://www.bbc.co.uk' + i.parent['href'] if i.parent['href'] != re.compile('^https')
                    else i.parent['href']}

            if news not in news_list:
                news_list.append(news)

        return news_list
