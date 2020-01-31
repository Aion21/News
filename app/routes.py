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
    ria = Ria().get_news()

    return render_template('ria.html', name='Ria', news=ria)


@app.route('/bbc')
def bbc():
    bbc = BBC().get_news()

    return render_template('bbc.html', name='BBC', news=bbc)


@app.route('/interfax')
def interfax():
    interfax = Interfax().get_news()

    return render_template('interfax.html', name='Interfax', news=interfax)


@app.route('/all')
def all():
    interfax = Interfax().get_news()
    bbc = BBC().get_news()
    ria = Ria().get_news()

    return render_template('all.html',
                           name='All',
                           interfax=interfax,
                           bbc=bbc,
                           ria=ria)
