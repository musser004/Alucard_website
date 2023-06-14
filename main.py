# Alucard business website project

from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from forms import ContactForm
from flask_ckeditor import CKEditor
import os
import gunicorn

# Initial Flask setup

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
Bootstrap(app)
ckeditor = CKEditor(app)

# Index page setup


@app.route("/", methods=["GET", "POST"])
def index():
    form = ContactForm()

    # Contact form setup

    if form.validate_on_submit():
        flash("Message successfully sent!")
        form.name.data = ""
        form.email.data = ""
        form.phone.data = ""
        form.message.data = ""
    return render_template("index.html", form=form)

# Portfolio project 1 page setup


@app.route("/portfolio-1")
def portfolio_1():
    return render_template("portfolio-1.html")

# Portfolio project 2 page setup


@app.route("/portfolio-2")
def portfolio_2():
    return render_template("portfolio-2.html")

# Portfolio project 3 page setup


@app.route("/portfolio-3")
def portfolio_3():
    return render_template("portfolio-3.html")

# Flask run


if __name__ == "__main__":
    app.run(debug=True)
