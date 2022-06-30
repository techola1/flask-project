from distutils.log import debug
from json.tool import main
from flask import Flask, jsonfy
import time

app = flask(__name__)

app.route ("/")
def hello_world():
    return jsonfy ({"time to call" time.time()})

if __name__ == "_main_":
    app.run(host= '0.0.0.0', debug=True)
    
