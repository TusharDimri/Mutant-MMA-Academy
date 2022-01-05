from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
mail = Mail(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contact", methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = "+91" + str(request.form.get('phone'))
    query = request.form.get('query')
    data = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nQuery: {query}\n"

    # Sending Mail from creater to owner:
    app.config["MAIL_SERVER"] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = os.getenv('EMAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASSWORD')
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    mail = Mail(app)
    msg = Message(
        subject="Query from website",
        sender=os.getenv('EMAIL_USERNAME'),
        recipients=["tushar.dimri22@gmail.com"]
    )
    msg.body = data
    mail.send(msg)
    return redirect(url_for("index"))


app.run(debug=True)
