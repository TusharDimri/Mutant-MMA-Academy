from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contact", methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    query = request.form.get('query')
    print(f"Name: {name}, Email: {email}, Query: {query}")
    return redirect(url_for("index"))


app.run(debug=True)
