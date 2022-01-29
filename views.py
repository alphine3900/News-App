from flask import Flask, render_template
from newsapi import NewsApiclient

app = Flask(__name__)


@app.route('/')
def index():
    newapi = NewsApiclient(api_key="6c9aad01acf44f5593688f40d255c0ca")
    topheadlines = newapi.get_top_headlines(sources="al-jazeera-english")

    articles = topheadlines['articles']
    desc = []
    news = []
    img = []
    time = []
    contet = []
    link = []


    for i in range(len(articles)):
        myarticles - articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles[''])
        time.append(myarticles[''])
        contet.append(myarticles[''])
        link.append(myarticles[''])


        my_list = zip(desc,contet,img)
        return render_template('index.html',context=my_list)

        if __name__   == "__main__":
            app.run(debug=True)