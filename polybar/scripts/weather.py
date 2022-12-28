import requests

OPENWEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
OPENWEATHER_API_KEY = "e7d3b7b890f2486e3adc4343bdf6f0cd"
lat = "39.76"
lon = "30.52"

def getWeather() -> dict[str, str] | None:
    try:
        req = requests.get(f"{OPENWEATHER_URL}?lat={lat}&lon={lon}&units=metric&appid={OPENWEATHER_API_KEY}")
        data = req.json()
        temp = data["main"]["temp"]
#        feels = data["main"]["feels_like"]
        desc = data["weather"][0]["description"]
        unit = "ºC"

        return {
            "temp": f"{int(temp)}{unit}",
 #           "feels": f"{int(feels)}{unit}",
            "desc": desc.title(),
                }
    except Exception:
        return None

def main() -> None:
    weather = getWeather()
    if weather:
        temp, desc = weather.values()
        print(f"{temp}, {desc}")

if __name__ == "__main__":
    main()
