from flask import Flask,request,jsonify
import requests

app = Flask(__name__)

@app.route("/", methods=['POST'])  # flask routing
def index():
    data = request.get_json()
    period_length = data['queryResult']['parameters']["periodlength"]
    period_cycle = data['queryResult']['parameters']["periodcycle"]
    last_period = data['queryResult']['parameters']["lastperiod"]
    return "Hello"

if __name__ == "__main__":
    app.run()