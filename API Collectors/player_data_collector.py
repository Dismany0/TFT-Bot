import requests
import key
import datetime
import time

def collect_challengers():
    URL = "https://na1.api.riotgames.com/tft/league/v1/challenger"\
    + "?api_key=" + key.API_KEY
    resp = requests.get(URL)

    if not resp:
        print("Error " + str(resp.status_code))
        return -1
    
    info = resp.json()

    #WRITE TO FILE
    f = open("DATA/Players/Challengers_" + str(datetime.date.today())+".txt", 'w')
    for player in info.get("entries"):
        try:
            f.write(player.get("summonerName") + \
                " || LP: " + str(player.get("leaguePoints")) + \
                    " Wins: " + str(player.get("wins")) + \
                        " Losses: " + str(player.get("losses")) + "\n")
        except:
            continue
    f.close()

    f = open("DATA/Players/Challengers_SID" + str(datetime.date.today())+".txt", 'w')
    for player in info.get("entries"):
        try:
            f.write(player.get("summonerId") + "\n")
        except:
            continue
    f.close()
    return info

def collect_grandmasters():
    URL = "https://na1.api.riotgames.com/tft/league/v1/grandmaster"\
    + "?api_key=" + key.API_KEY
    resp = requests.get(URL)
    info = resp.json()

    #WRITE TO FILE
    f = open("DATA/Players/Grandmasters_" + str(datetime.date.today())+".txt", 'w')
    for player in info.get("entries"):
        try:
            f.write(player.get("summonerName") + \
                " || LP: " + str(player.get("leaguePoints")) + \
                    " Wins: " + str(player.get("wins")) + \
                        " Losses: " + str(player.get("losses")) + "\n")
        except:
            continue
    f.close()

    f = open("DATA/Players/Grandmasters_SID" + str(datetime.date.today())+".txt", 'w')
    for player in info.get("entries"):
        try:
            f.write(player.get("summonerId") + "\n")
        except:
            continue
    f.close()
    return info

def collect_masters():
    URL = "https://na1.api.riotgames.com/tft/league/v1/master"\
    + "?api_key=" + key.API_KEY
    resp = requests.get(URL)
    info = resp.json()

        #WRITE TO FILE
    f = open("DATA/Players/Masters_" + str(datetime.date.today())+".txt", 'w')
    for player in info.get("entries"):
        try:
            f.write(player.get("summonerName") + \
                " || LP: " + str(player.get("leaguePoints")) + \
                    " Wins: " + str(player.get("wins")) + \
                        " Losses: " + str(player.get("losses")) + "\n")
        except:
            continue
    f.close()

    f = open("DATA/Players/Masters_SID" + str(datetime.date.today())+".txt", 'w')
    for player in info.get("entries"):
        try:
            f.write(player.get("summonerId") + "\n")
        except:
            continue
    f.close()
    return info


def convert_challengers():
    count = 1
    URL = "https://na1.api.riotgames.com/tft/summoner/v1/summoners/"
    f = open("DATA/Players/Challengers_SID" + str(datetime.date.today())+".txt", 'r')
    f2 = open("DATA/Players/Challengers_PUUID" + str(datetime.date.today())+".txt", 'w')
    for row in f:
        resp = requests.get(URL+row.strip()+"?api_key=" + key.API_KEY)
        info = resp.json()
        f2.write(str(info.get("puuid")) + "\n")
        print(str(count) + "/8000")
        count += 1
        time.sleep(1.22)
    f.close()
    f2.close()

def convert_grandmasters():
    count = 1
    URL = "https://na1.api.riotgames.com/tft/summoner/v1/summoners/"
    f = open("DATA/Players/Grandmasters_SID" + str(datetime.date.today())+".txt", 'r')
    f2 = open("DATA/Players/Grandmasters_PUUID" + str(datetime.date.today())+".txt", 'w')
    for row in f:
        resp = requests.get(URL+row.strip()+"?api_key=" + key.API_KEY)
        info = resp.json()
        f2.write(str(info.get("puuid")) + "\n")
        print(str(count+250) + "/8000")
        count += 1
        time.sleep(1.22)
    f.close()
    f2.close()

def convert_masters():
    count = 1
    URL = "https://na1.api.riotgames.com/tft/summoner/v1/summoners/"
    f = open("DATA/Players/Masters_SID" + str(datetime.date.today())+".txt", 'r')
    f2 = open("DATA/Players/Masters_PUUID" + str(datetime.date.today())+".txt", 'w')
    for row in f:
        resp = requests.get(URL+row.strip()+"?api_key=" + key.API_KEY)
        info = resp.json()
        f2.write(str(info.get("puuid")) + "\n")
        print(str(count+750) + "/8000 something")
        count += 1
        time.sleep(1.22)
    f.close()
    f2.close()


collect_challengers()
collect_grandmasters()
collect_masters()

convert_challengers()
convert_grandmasters()
convert_masters()