from app import app
from flask import render_template
from app.news.bbc import BBC
from app.news.interfax import Interfax
from app.news.ria import Ria


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/ria')
def ria():
    ria_news = Ria().parse()

    return render_template('news_page.html', title='Ria', news=[{'source_name': 'Ria', 'news': ria_news}])


@app.route('/bbc')
def bbc():
    bbc_news = BBC().parse()

    return render_template('news_page.html', title='BBC', news=[{'source_name': 'BBC', 'news': bbc_news}])


@app.route('/interfax')
def interfax():
    interfax_news = Interfax().parse()

    return render_template('news_page.html', title='Interfax',
                           news=[{'source_name': 'Interfax', 'news': interfax_news}])


@app.route('/all')
def all():
    interfax_news = Interfax().parse()
    bbc_news = BBC().parse()
    ria_news = Ria().parse()

    return render_template('news_page.html',
                           title='All news',
                           news=[{'source_name': 'Ria', 'news': ria_news},
                                 {'source_name': 'BBC', 'news': bbc_news},
                                 {'source_name': 'Interfax', 'news': interfax_news}])
