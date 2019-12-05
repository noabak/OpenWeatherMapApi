from flask import Flask, render_template
import requests

app=Flask(__name__)
'''
atraves de otra app le vamos a pasar a esta datos que nos va a pintar
'''
@app.route("/", methods=["GET"])
def index():
    query = "London,UK"
    unit = "metric"  # use "imperial" for Fahrenheit
    api_key = open("key.txt", "r").read()

    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}".format(query, unit, api_key)
    data = requests.get(url=url)  # GET request to the OpenWeatherMap API

    return render_template("index.html", data=data.json())

if __name__ =='__main__':
    app.run(debug=True,port="5001")