import requests

city_name = input("Enter city name:")
url= "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}".format(city_name)
res = requests.get(url)
data = res.json()

humidity = data['main']['humidity']
pressure= data['main']['pressure']
wind= data['main']['wind']
description= data['weather'][0]['description']
temp= data['main']['temp']

print("Temperature:", temp, "°C")
print("Wind:", wind)
print("Pressure:", pressure)
print("Humidity:", humidity)
print("Description:", description)