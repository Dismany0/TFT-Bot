import time


API_KEY = "RGAPI-b30dedbb-3bd8-484a-bbc7-e98d31a36efe"


















API_URL_BASE = "https://na1.api.riotgames.com"
API_URL_BASE_2 = "https://americas.api.riotgames.com"
API_URL_TFT_NAME = "/tft/summoner/v1/summoners/by-name/"
puuid = "tJ2sWQ6zLzMUsoVV0OfEOnQ2YMiBjh4_O1mmdGc62qC8dacMa3i5KWzCrp2YrIIno4Et35nZ_mzybg"
#Ray
API_URL_TFT_MATCH = "/tft/match/v1/matches/by-puuid/"+puuid+"/ids"

#BASE + Game + API + Search Type


NAME = "yikang"
API_GET_SUMMONER = API_URL_BASE + API_URL_TFT_NAME + NAME + "?api_key=" + API_KEY
start = "?start=0"
end = "&endTime="+ str(int(time.time()))
count = "&count=1&"
API_GET_MATCHES = API_URL_BASE_2 + API_URL_TFT_MATCH + start + end + count + "api_key=" + API_KEY

MATCH_ID = "NA1_4725067208"
API_GET_GAME = API_URL_BASE_2 + "/tft/match/v1/matches/" + MATCH_ID + "?api_key=" + API_KEY