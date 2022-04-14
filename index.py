from firebase_admin import db, credentials, initialize_app
import pyrebase
from flask import *
app = Flask(__name__)

auth = pyrebase.initialize_app({
        "apiKey": "AIzaSyAByWb1CzSlgk0OzSS2llwPnkVE7NWQbXw",
        "authDomain": "clyde-web.firebaseapp.com",
        "databaseURL": "https://clyde-web-default-rtdb.asia-southeast1.firebasedatabase.app",
        "projectId": "clyde-web",
        "storageBucket": "clyde-web.appspot.com",
        "messagingSenderId": "691435749279",
        "appId": "1:691435749279:web:f7b33ad28a2fd62be6c7aa",
        "measurementId": "G-722LG7913E"
    },).auth()
default_app = initialize_app(
    credentials.Certificate(
        {
            "type": "service_account",
            "project_id": "clyde-web",
            "private_key_id": "f2a916fc26ce3e818087d5d0b88c1d31d65e3f8f",
            "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC6BnNI8Xyn72/3\n9uqYay6s35XWC3r1IMOtbg2Hquqt+GpsdV47fP1Ds9CuNHaAcGRRzOzyTqUyO5gB\nPwvHgREz/wZ3lXOYPgn3aEQ0yT3jxracoLjMqj7v/ydfSzuka0TWW6/ov+DkQT6F\nLZ29yv5eujwg1QGQ+tlfPZ+LP4bhKCTAJi/GhKdRruoerV7/UPHhxbcfCoItmUNT\n8aMEb7XVFjhbjxkofu8hKiy46IAEVVZS+F6DkZmgmhVF0D0CqiglLhvuEC4u1Bc2\ngVWgvKwnLHCRm2gKs1YIO3WAI604BMhU+x4n3h+rJ3m4R6SC9xC5eidb2H2QXNrv\nOuvByXU3AgMBAAECggEAPKpS2WRrdybWGIMNIXS+zYDC0AGBcURkm//qaKZ8Dw0W\nw9UIzJSn0XboJI+WX6+Hf8e5NBIivH2DxlBFqqO0NQVDmicCghElVepKZ/6C8O/C\naNTfP1t71++ZavHRev7Cfbd76Ab/M+D1HyBvs0/qYYERj9F3R80Oq4kgqRwoA+/x\nop2bGo1FihRKrMbxA6joaDMXtDTMmTIUEq6fUSqkT009CM8SPclu1h554Suys+Jq\n29nVuPbFCJ+gmGngQcdzIT00540T9cBGgldvt3skMM9eHn9JaUZ9od/OrVGCIRqX\n7YAJaCVG8fXP51ozz35dlOqNBXfYoGLT31LyHuNztQKBgQDe0HNBQQYjOYUAVjby\nhhYXThdJvzC4NQPtqWh9hN5Hv8TirCfEjv0HB3FKBWoij4PIxDQoSP4//y01fJ0B\nIwTnAg0nTqy4cmDXET2wo9A2DGxsu0eZxZ1I/YOGRYJTmsGE54CqHd7yyV2YGwZT\n/jnvweX0S1G9ZkrDIhfYYxCFxQKBgQDVu0rSfbQ5a1XGDUTUzonIOCOxb5V07V6r\ndiXG5H1CY18wcenLWfAlD9rFd5ETg9yLvWN27jEhZq1d/FpBldQdDqRuMkHQRJn1\n20bXh7n+9baefKYt+rpTD5mqWp2GEcCQoXs1gXOFyrpUWYMhuVyv2vrVc0AuWm60\nLzQB2qn6ywKBgQCCqJwdlOLjfxRmOShpmYWUzv9LCKmqK7SNBn22tVafnm33Olrr\noanxGEUv0fMGJ0BxV9T6Fqu5nYrGRbfP9dgnGwXZmgIg+zmchIi3b6hmOWzPahc3\nrjFonvkkoNgm7KY0qIjDuVaG6txOmPJiCL+yv/J4Cj75oOWQfgqboqQKvQKBgFhn\n1Bck77sgbqYxLttnYw5ySjFGmmd3F8WMZSvTrwwa1nDPbYkzdmWeHTu4rUWJMVyL\nxeyXsbLDKcrKavrd4pLyT4lVOGvRNG3BeZgFCCYxtIvxuzshjph0x3bzbFzcUu6A\nHNqQ5RveMxxYuijk5zXGOiK4PT/vIANf0v9BVzXpAoGAEScgtmsDX+43W1S4KsEM\nCT1iT0B6nSVBpeq/esjOD9Rt1JCWSmOEUi6SquiD2wpxjQ1YZCTGkKsuj3KdwKPl\n0aeGgIKoUrhEAfkgxx11HvY6ZfuxxtPgN8nXbTtY6PK3iLjVT5OQ+AG0IOPRhR+0\np2XMA7vqgMDL8t96cfd/2Tk=\n-----END PRIVATE KEY-----\n",
            "client_email": "firebase-adminsdk-bo8th@clyde-web.iam.gserviceaccount.com",
            "client_id": "102820297151318096500",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-bo8th%40clyde-web.iam.gserviceaccount.com"
        }

    ),
    {
        "apiKey": "AIzaSyAByWb1CzSlgk0OzSS2llwPnkVE7NWQbXw",
        "authDomain": "clyde-web.firebaseapp.com",
        "databaseURL": "https://clyde-web-default-rtdb.asia-southeast1.firebasedatabase.app",
        "projectId": "clyde-web",
        "storageBucket": "clyde-web.appspot.com",
        "messagingSenderId": "691435749279",
        "appId": "1:691435749279:web:f7b33ad28a2fd62be6c7aa",
        "measurementId": "G-722LG7913E"
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


@app.route('/appointment')
def appointment():
    try:
        proxys = (db.reference(f"/profiles/")).get()
        datas = list(proxys.values())

        for data in datas:
            if data["role"] != "teacher":
                datas.remove(data)

        return render_template('appointment.html', datas=datas)
    except Exception as e:
        pass
    return render_template('appointment.html')


@app.route('/signup', methods=['GET', 'POST'])
def regester():
    try:
        email1 = request.cookies.get('email')
        password1 = request.cookies.get('password')
        info = auth.sign_in_with_email_and_password(email1, password1)
        details = auth.get_account_info(info["idToken"])
        if details["users"][0]["emailVerified"] != False:
            return redirect("/")
    except:
        pass
    if request.method == 'POST':
        try:
            firstname = request.form['firstname']
            lastnmae = request.form['lastnmae']
            email = request.form['email']
            company = request.form['company']
            ROLE = request.form['ROLE']
            address = request.form['address']
            password = "Is@290403"
            newuser = auth.create_user_with_email_and_password(
                email, password)
            auth.send_email_verification(newuser["idToken"])
            details = auth.get_account_info(newuser["idToken"])
            detail = {
                "firstname": firstname,
                "lastnmae": lastnmae,
                "email": email,
                "company": company,
                "role": ROLE,
                "address": address,
                "bio": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Ad, dicta? Magnam atque iste fugit neque.\nMagni possimus exercitationem ut voluptatibus eius incidunt, quo maxime illum, eos quis commodi,\nsaepe minima.",
                "uid": f"{details['users'][0]['localId']}",
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6VeVHSV-OV1ATnG7fcc-mCk06DEEfteHT5Q&usqp=CAU",
                "star": "1"
            }
            proxys = (db.reference(
                f"/profiles/{details['users'][0]['localId']}")).set(detail)
            if details["users"][0]["emailVerified"] == False:
                return render_template('login.html', s='Verify Your Email')
        except Exception as e:
            print(e)
            return render_template('regester.html', s='This Email Is Already Used')

    return render_template("regester.html")


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, threaded=True)
