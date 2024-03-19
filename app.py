from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def underConstruction():
    return render_template('underconstruction.html')
@app.route("/portfolio")
def portfolio():
    return render_template('underconstruction.html')
@app.route("/hackswift")
def hackswift():
    return render_template('underconstruction.html')