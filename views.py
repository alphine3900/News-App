
from flask import Flask, render_template
from newsapi import NewsApiClient


app = Flask(__name__)


@app.route('/')
def index():
    newapi = NewsApiClient(api_key="6c9aad01acf44f5593688f40d255c0ca")
    topheadlines = newapi.get_top_headlines(sources="al-jazeera-english")

    articles = topheadlines['articles']
    description = []
    news = []
    img = []
    # time = []
    content = []
    # link = []


    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        description.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        # time.append(myarticles['publishedAt'])
        content.append(myarticles['content'])
        # link.append(myarticles['url'])


        my_list = zip(description,content,img,news)
        return render_template('index.html', context=my_list)


@app.route('/home')
def home():
    newapi = NewsApiClient(api_key="6c9aad01acf44f5593688f40d255c0ca")
    topheadlines = newapi.get_top_headlines(sources="bbc-news")

    articles = topheadlines['articles']
    description = []
    news = []
    img = []
    # time = []
    content = []
    # link = []


    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        description.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        # time.append(myarticles['publishedAt'])
        content.append(myarticles['content'])
        # link.append(myarticles['url'])


        my_list = zip(description,content,img,news)
        return render_template('home.html', context=my_list)

# @app.route('/home')
# def home():
#     return render_template('home.html')
if __name__ == '__main__':
    app.run(debug = True)   