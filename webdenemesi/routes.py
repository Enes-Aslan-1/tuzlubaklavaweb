from webdenemesi import app
from flask import render_template

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/commands')
def commands():
    return render_template("commands.html", title = "Komutlar")