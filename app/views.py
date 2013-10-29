from flask import render_template, session, request, redirect, url_for
from app import app

@app.route("/")
@app.route("/index/", methods=["GET"])
def index():
    user = { 'nickname': 'Miguel' } # fake user
    friends = [{'name':'Jim Green','sex':'boy'},{'name':'Han Meimei','sex':'girl'}]
    return render_template("index.html", title = 'Home', user=user, friends=friends, c = len(friends))

@app.route("/index/", methods=["POST"])
def indexPost():
    return redirect(url_for('home',xx=request.form['xx']))

@app.route('/home/<xx>/')
def home(xx):
    return render_template("home.html", x=xx)