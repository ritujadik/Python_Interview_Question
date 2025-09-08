import redis
import json
import requests

client = redis.StrictRedis(host='localhost',port=6379,db=0)

API_URL = "https://api.weather.com/v3/weather/forecast"

def fetch_weather_data(location):
    cache_key = f"weather:{location}"
    cached_data = client.get(cache_key)

    if cached_data:
        print("Cache hit:Returning cached data")
        return json.loads(cached_data)

    print("Cache miss:Fetching data from external api")
    try:
        response = requests.get(API_URL,params={"location":location})
        if response.status_code == 200:
            data = response.json()
            client.setex(cache_key,300,json.dumps(data))
            return data
        else:
            print(f"failed to fetched the data.status_code:{response.status_code},Response:{response.text}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error during the request:{e}")
        return None

location = "Noida"
weather_data = fetch_weather_data(location)
if weather_data:
    print(weather_data)
else:
    print("could not fetch the data")

