import requests
import key
import datetime
import time
from Classes import *

Augments = dict()


def loadData(file:str):
    f = open("DATA/Augment Data/GM.txt", 'r')
    for row in f:
        info = row.strip().split(',')
        Augments[info[0]] = Augment(info[0], int(info[1]), float(info[2]),\
                                    float(info[3]), float(info[4]), float(info[5]),\
                                        float(info[6]), float(info[7]), int(info[8]), int(info[9]), int(info[10]))
    f.close()
    return 0

def collectAugmentData(file1:str, file2:str, rate:int):
    # f1 = open("DATA/Matches/Masters_Games2023-07-29.txt", 'r')
    f1 = open(file1, 'r')
    num = len(f1.readlines())
    line = 0
    for game in f1:
        print(str(line) + "/" + num)
        line += 1
        if(line % rate == 0):
            write(file2)
            print("UPDATING")
        try:
            URL = "https://americas.api.riotgames.com/tft/match/v1/matches/" + game.strip()\
            + "?api_key=" + key.API_KEY
            resp = requests.get(URL)
            info = resp.json()
            time.sleep(1.2)

            for player in info.get("info").get("participants"):
                augcounter = 1
                for augment in player.get("augments"):
                    #FOR EACH AUGMENT, FOR EACH PLAYER
                    if augment not in Augments:
                        Augments[augment] = Augment(augment, 0, 0.0,\
                                        0.0, 0.0, 0.0,\
                                            0.0, 0.0, 0, 0, 0)
                    if augment in Augments:
                        #Increase gamesplayed by 1
                        Augments[augment].gamesPlayed += 1
                        #If player wins, increase winrate, otherwise decrease
                        if player.get("placement") == 1:
                            Augments[augment].winrate = ((Augments[augment].winrate * (Augments[augment].gamesPlayed - 1)) + 1)/Augments[augment].gamesPlayed
                        else:
                            Augments[augment].winrate = (Augments[augment].winrate * (Augments[augment].gamesPlayed - 1))/Augments[augment].gamesPlayed
                        
                        #Top 4
                        if player.get("placement") <= 4:
                            Augments[augment].top4rate = ((Augments[augment].top4rate * (Augments[augment].gamesPlayed - 1)) + 1)/Augments[augment].gamesPlayed
                        else:
                            Augments[augment].top4rate = (Augments[augment].top4rate * (Augments[augment].gamesPlayed - 1))/Augments[augment].gamesPlayed
                        
                        #AveragePlacement
                        Augments[augment].averagePlacement = ((Augments[augment].averagePlacement * (Augments[augment].gamesPlayed - 1)) + player.get("placement"))/Augments[augment].gamesPlayed

                        if(augcounter == 1):
                            #2-1
                            Augments[augment].p2g += 1
                            Augments[augment].p2_1 = ((Augments[augment].p2_1 * (Augments[augment].p2g - 1)) + player.get("placement"))/Augments[augment].p2g
                        elif(augcounter == 2):
                            #3-2
                            Augments[augment].p3g += 1
                            Augments[augment].p3_2 = ((Augments[augment].p3_2 * (Augments[augment].p3g - 1)) + player.get("placement"))/Augments[augment].p3g
                        elif(augcounter == 3):
                            #4-2
                            Augments[augment].p4g += 1
                            Augments[augment].p4_2 = ((Augments[augment].p4_2 * (Augments[augment].p4g - 1)) + player.get("placement"))/Augments[augment].p4g

                        augcounter += 1
        except:
            continue
    f1.close()
    return 0

def write(file:str):
    # f2 = open("DATA/Augment Data/Masters.txt", 'w')
    f2 = open(file, 'w')
    for x in Augments:
        f2.write(Augments.get(x).__str__ + "\n")
        # f2.write(str(Augments.get(x).name) + "," + str(Augments.get(x).gamesPlayed) + "," + str(Augments.get(x).winrate) \
        #          + "," + str(Augments.get(x).top4rate) + "," + str(Augments.get(x).averagePlacement) + \
        #             "," + str(Augments.get(x).p2_1) + "," + str(Augments.get(x).p3_2) + \
        #                 "," + str(Augments.get(x).p4_2) + \
        #                     "," + str(Augments.get(x).p2g) +\
        #                         "," + str(Augments.get(x).p3g) +\
        #                             "," + str(Augments.get(x).p4g) +"\n")
    f2.close()


loadData()
collectAugmentData()
