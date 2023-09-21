import API_KEY
import requests
import json


key=API_KEY.Weather_API_KEY


city=input("Enter the city name-->")
url=f'https://api.weatherapi.com/v1/current.json?key={key}&q=%27{city}'
getRequest=requests.get(url).text
dic=json.loads(getRequest)

print("Temp(C): ",dic['current']['temp_c'])
print("Temp(f): ",dic['current']['temp_f'])
print("Temp(f): ",dic['current']['humidity'])

