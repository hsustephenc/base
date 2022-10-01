# -*- coding: utf-8 -*-
# to print results of certain bike and bus stations

"""
Spyder Editor

This is a temporary script file.
"""
 
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
 
 
import requests
import json

import pandas as pd


"""
response = requests.get("http://api.open-notify.org/astros.json")

response.json() # This method is convenient when the API returns JSON

query = {'lat':'45', 'lon':'180'}
response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)

"""

"""
station_id
name

1062807847
BNF - Bibliothèque Nationale de France

34742973
Place Balard
"""



start_date = '2021-05-04'
end_date = '2021-05-05'
dataset = 'comptage-velo-donnees-compteurs'
nrows = 2500 #Should be fine for about 1 day of data. Increase as required.


# resp = requests.get("https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json")

# resp = requests.get("https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_status.json")

"""
resp = requests.get("https://api.tfl.gov.uk/BikePoint")
a = resp.json()
print(json.dumps(a, indent=4))
"""


"""
list = [109,244,141,301,106]

for i in list:
    url = "https://api.tfl.gov.uk/BikePoint/BikePoints_" + str(i)
    resp = requests.get(url)
    a = resp.json()
 #   print(json.dumps(a, indent=4))
    print(a["commonName"])      
    print("Number of Bikes: " + a["additionalProperties"][6]["value"])
    print("Number of Standard Bikes: " + a["additionalProperties"][9]["value"])
    print("Number of E-Bikes: " + a["additionalProperties"][10]["value"])       
    print("Number of Empty Docks: " + a["additionalProperties"][7]["value"])
    x = pd.Timestamp(a["additionalProperties"][7]["modified"]).tz_convert('Europe/London')
    print("Last Updated: " + str(x))
    print("")

"""

# 490004005S Billingsate Market toward Limehouse
# 490004005N Billingsate Market toward Stratford

stations = ["490004005S", "490004005N"] 
 
for sta in stations:
    resp2 = requests.get("https://api.tfl.gov.uk/StopPoint/" + sta +"/Arrivals")
    a2 = resp2.json()
    print("Billingsgate Market towards " + (a2[0]["towards"]))
    print("")
    for i2 in a2:
        sec = i2["timeToStation"]
        left = sec%60
        min = (sec - left) / 60
        tim = pd.Timestamp(i2["expectedArrival"]).tz_convert('Europe/London')
        print(i2["lineName"] + " to " + i2["destinationName"])
        print("Expected in " + str(min) + " min & " + str(left) + " secs, at " + str(tim))
        print("")



# https://opendata.paris.fr/explore/dataset/comptage-velo-donnees-compteurs/information/?disjunctive.id_compteur&disjunctive.nom_compteur&disjunctive.id&disjunctive.name

# resp = requests.get("https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&q=&facet=name&facet=is_installed&facet=is_renting&facet=is_returning&facet=nom_arrondissement_communes&refine.name=%22Charonne+-+Robert+et+Sonia+Delauney%22")

url = (f"""\
https://opendata.paris.fr/api/records/1.0/search/\
?dataset={dataset}\
&q=date%3A%5B{start_date}T23%3A00%3A00Z+TO+{end_date}T22%3A59%3A59Z%5D\
&rows={nrows}\
&sort=-id&facet=id_compteur\
&facet=nom_compteur\
&facet=id\
&facet=name&facet=date\
&facet=installation_date\ 
""")

# resp = requests.get(url)

"""

resp = requests.get("https://api.nextbike.net/maps/nextbike-live.json")

print(resp)

a = resp.json()

print(a)


print(json.dumps(a, indent = 4, sort_keys=True))

"""
   
