from flask import Flask
from pages import Hackswift

app = Flask(__name__)

@app.route("/hackswift")
def Hackswift2024():
    return Hackswift