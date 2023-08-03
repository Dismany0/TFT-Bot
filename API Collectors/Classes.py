
class Champion:
    name = ""
    gamesPlayed = 0
    winrate = 0.0
    top4rate = 0.0
    averagePlacement = 0.0
    star1 = 0.0
    star2 = 0.0
    star3 = 0.0
    item1 = 0.0
    item2 = 0.0
    item3 = 0.0
    
    def __init__(self, name, gamesPlayed, winrate, top4rate, averagePlacement \
                 ,star1, star2, star3, item1, item2, item3):
        self.name = name
        self.gamesPlayed = gamesPlayed
        self.winrate = winrate
        self.top4rate = top4rate
        self.averagePlacement = averagePlacement
        self.star1 = star1
        self.star2 = star2
        self.star3 = star3
        self.item1 = item1
        self.item2 = item2
        self.item3 = item3
    def __str__(self):
        return f"{self.name},{self.gamesPlayed},{self.winrate},{self.top4rate},{self.averagePlacement}\
            ,{self.star1},{self.star2},{self.star3},{self.item1},{self.item2},{self.item3}"

class Tactician:
    name = ""
    gamesPlayed = 0
    winrate = 0.0
    top4rate = 0.0
    averagePlacement = 0.0
    
    def __init__(self, name, gamesPlayed, winrate, top4rate, averagePlacement):
        self.name = name
        self.gamesPlayed = gamesPlayed
        self.winrate = winrate
        self.top4rate = top4rate
        self.averagePlacement = averagePlacement
    def __str__(self):
        return f"{self.name},{self.gamesPlayed},{self.winrate},{self.top4rate},{self.averagePlacement}"

class Item:
    name = ""
    gamesPlayed = 0
    winrate = 0.0
    top4rate = 0.0
    averagePlacement = 0.0
    
    def __init__(self, name, gamesPlayed, winrate, top4rate, averagePlacement):
        self.name = name
        self.gamesPlayed = gamesPlayed
        self.winrate = winrate
        self.top4rate = top4rate
        self.averagePlacement = averagePlacement
    def __str__(self):
        return f"{self.name},{self.gamesPlayed},{self.winrate},{self.top4rate},{self.averagePlacement}"



class Augment:
    name = ""
    gamesPlayed = 0
    winrate = 0.0
    top4rate = 0.0
    averagePlacement = 0.0
    p2_1 = 0.0
    p3_2 = 0.0
    p4_2 = 0.0
    p2g = 0
    p3g = 0
    p4g = 0
    
    def __init__(self, name, gamesPlayed, winrate, top4rate, averagePlacement \
                 ,p2_1, p3_2, p4_2, p2g, p3g, p4g):
        self.name = name
        self.gamesPlayed = gamesPlayed
        self.winrate = winrate
        self.top4rate = top4rate
        self.averagePlacement = averagePlacement
        self.p2_1 = p2_1
        self.p3_2 = p3_2
        self.p4_2 = p4_2
        self.p2g = p2g
        self.p3g = p3g
        self.p4g = p4g
    def __str__(self):
        return f"{self.name},{self.gamesPlayed},{self.winrate},{self.top4rate},{self.averagePlacement}\
            ,{self.p2_1},{self.p3_2},{self.p4_2},{self.p2g},{self.p3g},{self.p4g}"
        