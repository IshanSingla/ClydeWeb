from flask import Flask, flash, jsonify, request, render_template, send_file, redirect
import firebase_admin
import asyncio
import os
import requests
import pyrebase
from datetime import datetime, date
from flask import *
app = Flask(__name__)
config = {
    "apiKey": "AIzaSyDCBuHPSO5Hbac8g995zNfAi9Puwh9osqA",
    "authDomain": "inducedmesssystem.firebaseapp.com",
    "databaseURL": "https://inducedmesssystem-default-rtdb.asia-southeast1.firebasedatabase.app/",
    "projectId": "inducedmesssystem",
    "storageBucket": "inducedmesssystem.appspot.com",
    "messagingSenderId": "1059758496051"
}

from firebase_admin import db, credentials
cred = credentials.Certificate("1.json")
default_app = firebase_admin.initialize_app(
    cred, {'databaseURL': "https://inducedmesssystem-default-rtdb.asia-southeast1.firebasedatabase.app/"})
auth = pyrebase.initialize_app(config).auth()

@app.route('/')
def home():
    email = request.cookies.get('email')
    password = request.cookies.get('password')
    try:
        info = auth.sign_in_with_email_and_password(email, password)
        details = auth.get_account_info(info["idToken"])
        if details["users"][0]["emailVerified"] == True:
            proxys = (db.reference(f"/Details/{info['localId']}/")).get()
            return render_template('index.html', s=proxys["Name"][0])
            return render_template('index.html', s=proxys["Name"])
    except Exception as e:
        pass
    return render_template('index.html')
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def basic():
    email1 = request.cookies.get('email')
    password1 = request.cookies.get('password')
    try:
        info = auth.sign_in_with_email_and_password(email1, password1)
        details = auth.get_account_info(info["idToken"])
        if details["users"][0]["emailVerified"] != False:
            return redirect("/")
    except:
        pass
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            try:
                newuser = auth.create_user_with_email_and_password(
                    email, password)
                auth.send_email_verification(newuser["idToken"])
                proxys = (db.reference(
                    f"/Details/{info['localId']}/Name")).set(name)
                details = auth.get_account_info(newuser["idToken"])
                if details["users"][0]["emailVerified"] == False:
                    return render_template('login.html', s='Verify Your Email')
                resp = make_response(render_template(
                    'login.html', s='Login successful'))
                resp.set_cookie('email', email, max_age=60*60*24)
                resp.set_cookie('password', password, max_age=60*60*24)
                return resp
            except:
                return render_template('login.html', s='This Email Is Already Used')
        except:
            try:
                email = request.form['email1']
                password = request.form['password1']
                try:
                    info = auth.sign_in_with_email_and_password(
                        email, password)
                    details = auth.get_account_info(info["idToken"])
                    if details["users"][0]["emailVerified"] == False:
                        return render_template('login.html', s='Verify Your Email')
                    resp = make_response(render_template(
                        'login.html', s='Login successful'))
                    resp.set_cookie('email', email, max_age=60*60*24)
                    resp.set_cookie('password', password, max_age=60*60*24)
                    return resp
                except:
                    return render_template('login.html', s='Invalid Password')
            except:
                pass
    return render_template('login.html', s="")


@app.route('/logout')
def logout():
    res = make_response(redirect("/login"))
    res.set_cookie('email', "", max_age=0)
    res.set_cookie('password', "", max_age=0)
    return res


@app.route('/passreset', methods=['GET', 'POST'])
def passreset():
    if request.method == 'POST':
        email = request.form['name']
        try:
            auth.send_password_reset_email(email)
            return render_template('new.html', s='Email Sendend successful')
        except:
            return render_template('new.html', us='Email Not Found')
    return render_template('new.html')


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
    return render_template("courcestemp.html", data=proxys)


@app.route('/doubt')
def doubt():
    return render_template("doubt.html")


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, threaded=True)
