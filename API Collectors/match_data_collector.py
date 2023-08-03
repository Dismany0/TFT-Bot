import requests
import key
import datetime
import time

Matches = set()

def collect_challenger():
    f = open("DATA/Players/Challengers_PUUID" + str(datetime.date.today())+".txt", 'r')
    f2 = open("DATA/Matches/Challengers_Games" + str(datetime.date.today())+".txt", 'w')
    counter = 1
    count = 30
    start = 0
    endTime = int(time.time())
    startTime = endTime - 172800

    for row in f:
        print(str(counter) + "/750")
        counter += 1
        URL = "https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/"\
        + row.strip() + "/ids?start=" + str(start) + "&endTime=" + str(endTime)\
        + "&startTime=" + str(startTime) + "&count=" + str(count) + \
        "&api_key=" + key.API_KEY
        resp = requests.get(URL)
        info = resp.json()
        time.sleep(1.22)
        for match    in info:
            if match in Matches:
                continue
            else:
                Matches.add(match)
                f2.write(match + "\n")

    f.close()
    f2.close()
    return 0

def collect_grandmaster():
    f = open("DATA/Players/Grandmasters_PUUID" + str(datetime.date.today())+".txt", 'r')
    f2 = open("DATA/Matches/Grandmasters_Games" + str(datetime.date.today())+".txt", 'w')
    counter = 1
    count = 30
    start = 0
    endTime = int(time.time())
    startTime = endTime - 172800

    for row in f:
        print(str(counter + 250) + "/750")
        counter += 1
        URL = "https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/"\
        + row.strip() + "/ids?start=" + str(start) + "&endTime=" + str(endTime)\
        + "&startTime=" + str(startTime) + "&count=" + str(count) + \
        "&api_key=" + key.API_KEY
        resp = requests.get(URL)
        info = resp.json()
        time.sleep(1.22)
        for match    in info:
            if match in Matches:
                continue
            else:
                Matches.add(match)
                f2.write(match + "\n")

    f.close()
    f2.close()
    return 0

def collect_master():
    f = open("DATA/Players/Masters_PUUID" + str(datetime.date.today())+".txt", 'r')
    f2 = open("DATA/Matches/Masters_Games" + str(datetime.date.today())+".txt", 'w')
    counter = 1
    count = 30
    start = 0
    endTime = int(time.time())
    startTime = endTime - 172800

    for row in f:
        print(str(counter + 750) + "/8000 something")
        counter += 1
        URL = "https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/"\
        + row.strip() + "/ids?start=" + str(start) + "&endTime=" + str(endTime)\
        + "&startTime=" + str(startTime) + "&count=" + str(count) + \
        "&api_key=" + key.API_KEY
        resp = requests.get(URL)
        info = resp.json()
        time.sleep(1.22)
        for match    in info:
            if match in Matches:
                continue
            else:
                Matches.add(match)
                f2.write(match + "\n")

    f.close()
    f2.close()
    return 0

collect_challenger()
collect_grandmaster()
collect_master()