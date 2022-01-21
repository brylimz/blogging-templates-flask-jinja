import requests.utils
from flask import Flask, render_template
import random
import datetime
import requests
app = Flask(__name__)
MY_NAME = "Bryan"


@app.route('/')
def home():
    current_year = datetime.date.today().year
    name_footer = MY_NAME
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, footer_year=current_year, footer_name=name_footer)


@app.route("/guess/<string:guess>")
def guess_name(guess):
    NAME = guess
    parameters_name = {
        "name": NAME
    }

    def gender():
        response = requests.get("https://api.genderize.io", params=parameters_name)
        response.raise_for_status()
        data = response.json()["gender"]
        return data

    def age():
        response2 = requests.get("https://api.agify.io/", params=parameters_name)
        response2.raise_for_status()
        data2 = response2.json()["age"]
        return data2

    return f"<h1> Hey {guess.title()}  </h1>" \
           f"<h2> <p> I think you are {gender()} </p> </h2>" \
           f"<h3> And maybe {age()} years old "


@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/c1bf880e51ba42a7416a"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)