
from flask import Flask, render_template
from newsapi import NewsApiClient


app = Flask(__name__)


@app.route('/')
def index():
    newapi = NewsApiClient(api_key="6c9aad01acf44f5593688f40d255c0ca")
    topheadlines = newapi.get_top_headlines(sources="al-jazeera-english")

    articles = topheadlines['articles']

    news = []
    description = []
    link = []
    img = []
    time = []
    content = []
   


    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        description.append(myarticles['description'])
        link.append(myarticles['url'])
        img.append(myarticles['urlToImage'])
        time.append(myarticles['publishedAt'])
        content.append(myarticles['content'])
       


        my_list = zip( news,description,link,img,time,content)
        return render_template('index.html', context=my_list)



@app.route('/home')
def home():
    newapi = NewsApiClient(api_key="6c9aad01acf44f5593688f40d255c0ca")
    topheadlines = newapi.get_top_headlines(sources="bbc-news")

    articles = topheadlines['articles']

    news = []
    description = []
    link = []
    img = []
    time = []
    content = []
   


    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        description.append(myarticles['description'])
        link.append(myarticles['url'])
        img.append(myarticles['urlToImage'])
        time.append(myarticles['publishedAt'])
        content.append(myarticles['content'])
       


        
    my_list = zip( news,description,link,img,time,content)
    return render_template('home.html', context=my_list)









@app.route('/entertainment')
def entertainment():
    newapi = NewsApiClient(api_key="6c9aad01acf44f5593688f40d255c0ca")
    topheadlines = newapi.get_top_headlines(sources="News24")

    articles = topheadlines['articles']
    news = []
    description = []
    link = []
    img = []
    time = []
    content = []


    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        description.append(myarticles['description'])
        link.append(myarticles['url'])
        img.append(myarticles['urlToImage'])
        time.append(myarticles['publishedAt'])
        content.append(myarticles['content'])
       


    my_list = zip( news,description,link,img,time,content)
    return render_template('entertainment.html', context=my_list)


@app.route('/health')
def health():
    newapi = NewsApiClient(api_key="6c9aad01acf44f5593688f40d255c0ca")
    topheadlines = newapi.get_top_headlines(sources="News24")

    articles = topheadlines['articles']
    news = []
    description = []
    link = []
    img = []
    time = []
    content = []


    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        description.append(myarticles['description'])
        link.append(myarticles['url'])
        img.append(myarticles['urlToImage'])
        time.append(myarticles['publishedAt'])
        content.append(myarticles['content'])
       


    my_list = zip( news,description,link,img,time,content)
    return render_template('health.html', context=my_list)

if __name__ == '__main__':
    app.run(debug = True)   