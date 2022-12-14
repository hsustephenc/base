 

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
    
    list = [109,141,301]
    for i in list:
        url = "https://api.tfl.gov.uk/BikePoint/BikePoints_" + str(i)
        resp = requests.get(url)
        a = resp.json()
        a1 = a["commonName"] + "<br>"
        a21 = "Number of Standard Bikes: " + a["additionalProperties"][9]["value"] + "<br>"
        a22 = "Number of E-Bikes: " + a["additionalProperties"][10]["value"] + "<br>"
        a3 = "Number of Empty Docks: " + a["additionalProperties"][7]["value"] + "<br>"
        x = pd.Timestamp(a["additionalProperties"][7]["modified"]).tz_convert('Europe/London')
        a4 = "Last Updated: " + str(x) + "<br>" + "<br>"
        sum = a1 + a21 + a22 + a3 + a4
        total = total + sum
        
      
    stations = {"490004005S":"Crossharbour / Limehouse","490004005N":"Bow / Leamouth"}
    c = "<b>Bus</b><br><br>"
    
    for sta,nam in stations.items():
        try:
            c4 = ""         
            resp2 = requests.get("https://api.tfl.gov.uk/StopPoint/" + sta +"/Arrivals")
            b2 = resp2.json()
            c1 = "<b>Billingsgate Market towards " + (b2[0]["towards"]+ "</b><br><br>")
            for i2 in b2:
                sec = i2["timeToStation"]
                left = sec%60
                min = (sec - left) / 60
                tim = pd.Timestamp(i2["expectedArrival"]).tz_convert('Europe/London')
                c2 = i2["lineName"] + " to " + i2["destinationName"] + "<br>"
                c3 = "Expected in " + str('{:.0f}'.format(min)) + " min & " + str(left) + " secs, at " + str(tim) + "<br><br>"
                c4 = c4 + c2 + c3
            c = c + c1 + c4

        except:
            c = c + "Station Billingsgate Market towards " + nam + " has no arrivals currently" + "<br><br>"
            
    total = total + c
    
    u = "<b>Velib</b><br><br>"
    
    try:
        resp3 = requests.get("https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_status.json")
        w = resp3.json()
        x=w["data"]["stations"]
        
        vstations = {66505516:"Cordeli??res - Arago",210749865:"Port-Royal - H??pital du Val-de-Gr??ce",54000550:"Rapp - Place du G??n??ral Gouraud"}
        
        for v,s in vstations.items():
            for j in x:
                if j["station_id"] == v:
                    u1 = s + "<br>"
                    u2 = "V??lib m??canique(s): " + str(j["num_bikes_available_types"][0]["mechanical"]) + "<br>"
                    u3 = "V??lib ??lectrique(s): " + str(j["num_bikes_available_types"][1]["ebike"]) + "<br>"
                    u4 = "Place(s): " + str(j["numDocksAvailable"]) + "<br><br>"
                    u = u + u1 + u2 + u3 + u4
    except:
        u = u + "Sorry the Velib thing doesn't work<br>"
        
    total = total + u
    
    resp4 = requests.get("https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Transportation_WebMercator/MapServer/5/query?where=1%3D1&outFields=*&outSR=4326&f=json")
    d = resp4.json()
    e = d["features"]
    
    stas = ["386","85"]
    h = "<b>Capital Bikes</b><br><br>"

    for st in stas:
        for f in e:
            g = f["attributes"]
            if g["STATION_ID"] == st:
                h1 = g["NAME"] + "<br>"
                h2 = "Number of Standard Bikes: " + str(g["NUM_BIKES_AVAILABLE"]) + "<br>"
                h3 = "Number of E-Bikes: " + str(g["NUM_EBIKES_AVAILABLE"]) + "<br>"
                h4 = "Number of Empty Docks: " + str(g["NUM_DOCKS_AVAILABLE"]) + "<br><br>"
                h = h + h1 + h2 + h3 + h4

    total = total + h

    return total


if __name__ == "__main__":
    app.run(debug=False)
