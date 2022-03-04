# Powered by postman
import requests
import time

def getWeather():
    city = input("Ingresa el nombre de la ciudad : ")
    api = "http://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=495c77767f823e18b72f055262e0251c"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    min_temp= int(json_data['main']['temp_min']-273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    temp = int(json_data['main']['temp_max']-273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + str(temp)+"ºC"
    final_data = "\n" + "Max Temp: " + str(max_temp) + "\n" + "Min Temp: " + str(min_temp)+ "\n" + "Pressure " + str(pressure) + "\n" + "humidity" + str(humidity) + "\n" + "WInd Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + '\n' + "Sunset: " + sunset

    print(final_info)
    print(final_data)

print(getWeather())





