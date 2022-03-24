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
def home():
    return render_template("index.html")


@app.route('/login')
def api():
    return render_template("login.html")

@app.route('/home')
def api():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, threaded=True)
