from flask import Flask, flash, jsonify, request, render_template, send_file, redirect
import firebase_admin,asyncio,os,requests
from firebase_admin import db, credentials
from datetime import datetime, date


cred = credentials.Certificate('1.json')
default_app = firebase_admin.initialize_app(
    cred, {'databaseURL': "https://clyde-web-default-rtdb.asia-southeast1.firebasedatabase.app/"})

app = Flask(__name__)

app.secret_key = 'i_iz_noob'
loop = asyncio.get_event_loop()


@app.route('/')
def _():
    return render_template("index.html")


@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/tutor')
def tutor():
    return render_template("tutor.html")

@app.route('/cources')
def courses():
    return render_template("cources.html")

@app.route('/cources/<string:n>')
def cources(n):
    proxys = (db.reference(f"/Courses/{n}/")).get()
    if proxys == None:
        return render_template("404.html")
    return render_template("courcestemp.html",data=proxys)

@app.route('/doubt')
def doubt():
    return render_template("doubt.html")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, threaded=True)
