import nltk
from newspaper import Article

from flask import Flask, redirect, url_for, render_template, request


app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        url = request.form["url"]
       
        article = Article(url)
        article.download() 
        article.parse() 
        nltk.download('punkt') 
        article.nlp()

        #Get the authors
        author = article.authors[0]

        #Get the title
        title = article.title

        #Get the publish date 
        date = article.publish_date

        #Get a summary of the article
        sum = article.summary

        return redirect(url_for("summary", author=author, title=title, date = date, sum = sum))

    else:
        return(render_template("index.html"))


@app.route("/<author>/<title>/<date>/<sum>")
def summary(author,title,date,sum):
    return render_template("summary.html", author=author, title=title, date=date,summary=sum)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)