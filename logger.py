import requests
import json
print("logger.py has successfully loaded.")
print("APIs used: IP2Location, Ipify, Geocode.maps.co.")
print("1 for another person.")
print("2 for your IP address.")
requestType = input("Are you tracking another person or getting your own IP: ")

def getInformation(type, address):
    if type == "myself":
        key = "439A18D14BF8EA771513CC94CA27057A"
        informationLogURL = "https://api.ip2location.io/?key=" + key + "&ip="
        addressLogURL = "https://api.ipify.org?format=json"
        addressPhase = requests.get(addressLogURL).text
        address = json.loads(addressPhase)["ip"]
        information = requests.get(informationLogURL + address).text
        convertedinformation = json.loads(information)
        requestURL = "https://geocode.maps.co/reverse?lat="+str(convertedinformation["latitude"])+"&lon="+str(convertedinformation["longitude"])+"&api_key=664846b4a622b397843773wcda16a6f"
        geolocationPhase = requests.get(requestURL)
        print(information)
        print(geolocationPhase.text)
    else:
        key = "439A18D14BF8EA771513CC94CA27057A"
        informationLogURL = "https://api.ip2location.io/?key=" + key + "&ip="
        information = requests.get(informationLogURL + address).text
        convertedinformation = json.loads(information)
        requestURL = "https://geocode.maps.co/reverse?lat="+str(convertedinformation["latitude"])+"&lon="+str(convertedinformation["longitude"])+"&api_key=664846b4a622b397843773wcda16a6f"
        geolocationPhase = requests.get(requestURL)
        print(information)
        print(geolocationPhase.text)

if requestType == "1":
    otherAddress = input("Enter the other person's IP: ")
    getInformation("anotherPerson", otherAddress)
else:
    getInformation("myself", "None")
