import requests
import key

# URL = key.API_GET_SUMMONER
# resp = requests.get(URL)
# info = resp.json()
# print(info)

URL = "https://na1.api.riotgames.com/tft/summoner/v1/summoners/by-name/"
resp = requests.get(URL)
info = resp.json()

print(info)

print(key.API_GET_GAME)