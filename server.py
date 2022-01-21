from flask import Flask, render_template
import random
import datetime
app = Flask(__name__)
MY_NAME = "Bryan"


@app.route('/')
def home():
    current_year = datetime.date.today().year
    name_footer = MY_NAME
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, footer_year=current_year, footer_name=name_footer)


if __name__ == "__main__":
    app.run(debug=True)