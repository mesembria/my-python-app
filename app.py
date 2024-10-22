from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    r = requests.get('https://api.ipify.org?format=json')
    myip = r.json().get('ip', 'unknown')
    return f"Hello, World from {myip}!"
