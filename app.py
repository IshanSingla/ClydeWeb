from firebase_admin import db, credentials, initialize_app
import pyrebase
from flask import *
app = Flask(__name__)

auth = pyrebase.initialize_app({
    "apiKey": "AIzaSyDCBuHPSO5Hbac8g995zNfAi9Puwh9osqA",
    "authDomain": "inducedmesssystem.firebaseapp.com",
    "databaseURL": "https://inducedmesssystem-default-rtdb.asia-southeast1.firebasedatabase.app/",
    "projectId": "inducedmesssystem",
    "storageBucket": "inducedmesssystem.appspot.com",
    "messagingSenderId": "1059758496051"
}).auth()
default_app = initialize_app(
    credentials.Certificate(
        {
            "type": "service_account",
            "project_id": "inducedmesssystem",
            "private_key_id": "c9a7d683768821fb449118c1d54199e093e5342f",
            "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDLKxiX1farl7jT\nCMo3s5bTPZ9e4s3owC7GfeSVAxpJM5hpLcD0IzKTzKHkQwsmMpXTPoJyYMkTMC1D\nmYIORo1vOeFWVIXIDqkvS+hZTneLozPkCmlFrnXeLAwg48hd2XrzPQg8njSaSHnY\nSHqTzxOiWcr2LOF63a5eA17qe6cTAwjyo4s8av6dythBTpm+JHPgMGdvZVK4P2EU\ng3/AgL45lxHGJ7K11964u3C/Z6cKnnxekOFW5A7wPlAL5na2lJqbFtCUOurbuT75\nvjrzA0dA1RG5N4f+s4ujPRsO94RhpsHGX/d93/qLO0S/P932vg9veVL5cPfU7v4c\nFDaSx3RDAgMBAAECggEADAetPbBb9aUf8ay6/t3tJX86Uk24Rvq6OAfCB3wyZ2am\nIoaALKtvuqr4ZDRIpUrxgMARFeFIq0dWb/COcAjQ3NSVsFQWnrFfizX4k4N17T0N\nPPZekff7KG5Y+YBxDWIit1D6+04uRzIiSWuqZCK9HlBxqm6Mv/SRiW5qzqZ04P4Q\nOKQsqtvfUzqt/DM7VpVGIKL1nk3LtZZTfmQoG5TjwPox/ius3CIgGixu9neAIP/+\nY+krQhO2i7rg3zYMug1Nm7kB8/gUAy2Cw3+MbO11Y7sk8DkSRPYUr+ecvq7cwoJK\n1J6SrjQjRKVg9H+0LVrCIoHIsYQYlWUvbtKLGPi1oQKBgQD0+0FifGPFShpPDL0b\ntx6obgSSIWpxQIcVO2ECJrM+LWmtdK4bUHebwghQD6SoF0B0x+69+SMKBQO4AYG/\neBqGlHjU2lpN2v+BSWCAT7bR930qh3hOzNfRKZVWf7zYe271kY8Gf4acCte5NTbd\ndUjE6JAXe4me3qI7EXNabNrF7QKBgQDUTmZLfr07RWIfH+fPontwDj2D3wnwlk8D\nRZynAmI4hsCXTFBDm7oAoo/+mw3qv/DJUcCdSkt6CtaLT91ZosSDsSLnwfYaDhU3\na9TRmgOWfpLuGM9Ob1GmGdj+sAOFGBQCoxmq03PZMOsvqTRsBeHkXDSt1cxxtL3C\nqf5pBBXc7wKBgGLdQvXL3TexQAzGx0p4DBdMzutqMNqjf+BBplSH6a4eBZfKjrjX\nMG3bUB9/MKPlPk3ioaZo9IsGmwmXEhWDErFdGaZMuETTLGmwgxFFGjKB/jE7moGy\niSYP8gSGaF+08IKJy36D2H8AoS5NG2cj/cn5UK0pXdCPaEkOMc88Ps3BAoGAQNGi\n57/NNJBtccVC+CDKgR7H50Asf7jUbNJPDqpqpIl3uXnCM7IS6ui2/+wFJrvtXvnH\nzf4F5z/x2tzKXviT+QUW/B067x+HmMEiW9Ai8kq4v1rxyCeyjPztRG0m1fbQ/TEg\nwAgJIbGOzKFjcOum2RrRtpVE8x5UpV9TXmqx5h8CgYABsAJMTbHo1TgHRHihNqAe\n7EdI0PZmoMgdq/oh8UkRyAYxLoximytA2R9IOvnsr5Kizz56ay1A2BFNVL6ZLg9O\ng0zOg2BE858RTj2CGQSmK0El+JlP0xoVX2OdPxCkId8oB8aq5s3rqPMsEYzCieNX\nbDwST+SH+tofsFOJbrtj7w==\n-----END PRIVATE KEY-----\n",
            "client_email": "firebase-adminsdk-hffym@inducedmesssystem.iam.gserviceaccount.com",
            "client_id": "111608122596104436421",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-hffym%40inducedmesssystem.iam.gserviceaccount.com"
        }
    ),
    {
        "apiKey": "AIzaSyDCBuHPSO5Hbac8g995zNfAi9Puwh9osqA",
        "authDomain": "inducedmesssystem.firebaseapp.com",
        "databaseURL": "https://inducedmesssystem-default-rtdb.asia-southeast1.firebasedatabase.app/",
        "projectId": "inducedmesssystem",
        "storageBucket": "inducedmesssystem.appspot.com",
        "messagingSenderId": "1059758496051"
    },
)


@app.route('/')
def home():
    email = request.cookies.get('email')
    password = request.cookies.get('password')
    try:
        info = auth.sign_in_with_email_and_password(email, password)
        details = auth.get_account_info(info["idToken"])
        if details["users"][0]['emailVerified'] == True:
            proxys = (db.reference(f"/Details/{info['localId']}/")).get()
            if proxys != None:
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
                details = auth.get_account_info(newuser["idToken"])
                proxys = (db.reference(
                    f"/Details/{details['users'][0]['localId']}/Name")).set(name)
                if details["users"][0]["emailVerified"] == False:
                    return render_template('login.html', s='Verify Your Email')
                resp = make_response(render_template(
                    'login.html', s='Login successful'))
                resp.set_cookie('email', email, max_age=60*60*24)
                resp.set_cookie('password', password, max_age=60*60*24)
                return resp
            except Exception as e:
                print(e)
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
                    resp.set_cookie('email', email, max_age=60*60)
                    resp.set_cookie('password', password, max_age=60*60)
                    return resp
                except:
                    return render_template('login.html', s='Invalid Password')
            except:
                pass
    return render_template('login.html', s="")


@app.route('/logout')
def logout():
    res = make_response(redirect("/"))
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


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, threaded=True)
