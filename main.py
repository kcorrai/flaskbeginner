from flask import Flask
import random
from passgen import gen_pass

facts_list = ['Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.',"2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.","Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir"]

app = Flask(__name__)

@app.route("/")
def h1():
    return '<h1>Hello World!<h1/><br><a href="/gercek" target="_blank">Rastgele bir gerçeği görüntüle!</a><br><a href="/sifre" target="_blank">Rastgele Şifre Oluştur!</a><br><a href="/yazitura" target="_blank">Yazi Tura Oyunu</a>'

@app.route("/gercek")
def hello_world():
    return f'<p>{random.choice(facts_list)}</p><br><a href="/">Anasayfa</a>'

@app.route("/sifre")
def sifre():
    return f'<h2>{gen_pass(10)}</h2><br><a href="/">Anasayfa</a>'

@app.route("/yazitura")
def yazitura():
    x = random.randint(0,1)
    if x == 1:
        return '<h1>Yazi Geldi</h1><br><a href="/">Anasayfa</a>'
    elif x == 0:
        return '<h1>Tura Geldi</h1><br><a href="/">Anasayfa</a>'

app.run(debug=True)
