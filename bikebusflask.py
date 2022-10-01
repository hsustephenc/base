 

# A very simple Flask Hello World app for you to get started with...
# flask version version of the bus and bike app


from flask import Flask
import requests
import json
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():

    total = ""
    list = [109,244,141,301,106]
    for i in list:
        url = "https://api.tfl.gov.uk/BikePoint/BikePoints_" + str(i)
        resp = requests.get(url)
        a = resp.json()
        a1 = a["commonName"] + "<br>"
        a2 = "Number of Bikes: " + a["additionalProperties"][6]["value"] + "<br>"
        a21 = "Number of Standard Bikes: " + a["additionalProperties"][9]["value"] + "<br>"
        a22 = "Number of E-Bikes: " + a["additionalProperties"][10]["value"] + "<br>"
        a3 = "Number of Empty Docks: " + a["additionalProperties"][7]["value"] + "<br>"
        x = pd.Timestamp(a["additionalProperties"][7]["modified"]).tz_convert('Europe/London')
        a4 = "Last Updated: " + str(x) + "<br>" + "<br>"
        sum = a1 + a2 + a21 + a22 + a3 + a4
        total = total + sum
        
    stations = ["490004005S", "490004005N"] 
    c = ""
    c4 = ""
    
    for sta in stations:
        resp2 = requests.get("https://api.tfl.gov.uk/StopPoint/" + sta +"/Arrivals")
        b2 = resp2.json()
        c1 = "<b>Billingsgate Market towards " + (b2[0]["towards"]+ "</b><br><br>")
        for i2 in b2:
            sec = i2["timeToStation"]
            left = sec%60
            min = (sec - left) / 60
            tim = pd.Timestamp(i2["expectedArrival"]).tz_convert('Europe/London')
            c2 = i2["lineName"] + " to " + i2["destinationName"] + "<br>"
            c3 = "Expected in " + str(min) + " min & " + str(left) + " secs, at " + str(tim) + "<br><br>"
            c4 = c4 + c2 + c3
        c = c + c1 + c4
    total = total + c

    return total


if __name__ == "__main__":
    app.run(debug=False)