from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' } # fake user
    friends = [{'name':'Jim Green','sex':'boy'},{'name':'Han Meimei','sex':'girl'}]
    return render_template("index.html", title = 'Home', user = user, friends = friends, c = len(friends))