import requests
import key
import time



def get_TFT_Summoner(name: str):
    #Gets the summoner data from a username
    #TODO Catch error, summoner not found, API not valid

    URL = "https://na1.api.riotgames.com/tft/summoner/v1/summoners/by-name/" \
        + name + "?api_key=" + key.API_KEY
    resp = requests.get(URL)
    info = resp.json()

    return info



def get_Match_History(puuid: str, start:str, endTime:str, count:int):
    #get the match history from start time to end time, and get count number of games

    #temp values
    start = 0
    endTime = str(int(time.time()))
    count = 20

    #TODO Check errors

    URL = "https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/" \
    + puuid + "/ids"
    URL += "?start=" + start + "&endTime=" + endTime + "&count=" + count + "&api_key=" + key.API_KEY
    resp = requests.get(URL)
    info = resp.json()
    return info

def get_Match(id: str):
    #Get the details from one single match
    #TODO ERROR CHECK

    URL = "https://americas.api.riotgames.com/tft/match/v1/matches/" + \
    id + "?api_key=" + key.API_KEY
    resp = requests.get(URL)
    info = resp.json()
    return info

