from flask import Flask, render_template, request, redirect, flash, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os
import datetime


load_dotenv()

bikash = '01705506169'
nogod = '01328137444'
load_dotenv()  # Load .env variables

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

mail = Mail(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/buy')
def buy_course():
    return render_template('classbay.html')


@app.route('/buy_2K')
def buy_2K():
    return render_template('BuyAll.html')


@app.route('/programming')
def programming():
    return render_template('programming.html')


@app.route('/buy?course=HTML%20%26%20CSS')
def buy(course=None):
    return render_template('BuyAll.html')


@app.route('/buy21')
def buyJS():
    return render_template('BuyAll.html')


@app.route('/buy1')
def buy1():
    return render_template('BuyAll.html')


@app.route('/buy5')
def buy5():
    return render_template('BuyAll.html')


@app.route('/buy4')
def buy4():
    return render_template('BuyAll.html')


@app.route('/buy2')
def buy2():
    return render_template('BuyAll.html')


@app.route('/submit_all', methods=['GET', 'POST'])
def submit_all():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        course_name = request.form.get('course_name')

        if not all([name, email, phone, course_name]):
            return "সব ফিল্ড পূরণ করুন", 400

        msg = Message(
            subject="Registration Successful",
            sender=app.config['MAIL_USERNAME'],
            recipients=['gamerthaking29@gmail.com'],
            body=f'''
                Name: {name}
                Phone: {phone}
                Email: {email}
                Course Name: {course_name}
                '''
        )
        try:
            mail.send(msg)
        except Exception as e:
            return f"Mail sending failed: {str(e)}"

        usermail = Message(
            subject="Registration Successful",
            sender=app.config['MAIL_USERNAME'],
            recipients=[email],
            body=f'''
                Web: {name} Thanks for Registering
            '''
        )
        try:
            mail.send(usermail)
        except Exception as e:
            return f"Mail sending failed: {str(e)}"

        # Note: stripe integration not included here since stripe is not imported or setup
        # Remove or comment out this part or add stripe setup if you want to use it.

        return "Registration successful!"

@app.route('/clash')
def clash():
    return render_template('clash.html')

@app.route('/live')
def live_class():
    today = datetime.datetime.today().weekday()
    if today in [4, 5]:  # শুক্রবার ও শনিবার
        zoom_link = "https://zoom.us/j/1234567890"  # তোমার Zoom Meeting URL
        return render_template('live.html', zoom_link=zoom_link)
    else:
        return render_template('class_closed.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
