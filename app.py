from flask import Flask,request,jsonify
import requests
from datetime import datetime
from datetime import timedelta 


app = Flask(__name__)

@app.route('/',methods=['POST'])  # flask routing
def index():
    data = request.get_json()
    period_length = data['queryResult']['parameters']["periodlength"]
    period_cycle = data['queryResult']['parameters']["periodcycle"]
    last_period = data['queryResult']['parameters']["lastperiod"]
    print(period_length)
    print(period_cycle)
    print(last_period)
    sum_days = int(period_length) + int(period_cycle)
    print(sum_days)
    current_date_temp = datetime.strptime(last_period, "%d/%m/%Y")
    print(current_date_temp)
    newdate = current_date_temp + timedelta(days=sum_days)
    newdate = newdate.strftime("%d/%m/%Y")
    response = {
        'fulfillmentText':"Your next period on🩸: {}".format(newdate)
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)