from collections import defaultdict

class Player:
    def __init__(self, username=None):
        self.username = username
        self.zergGames = 0
        self.protossGames = 0
        self.terranGames = 0
        
        #raceStats = {'replays': defaultdict(list), 'percent': 0}
        raceStats = defaultdict(lambda: {'replays': [], 'percent': 0})

        self.buildOrders = {"zerg": defaultdict(lambda: {'replays': [], 'percent': 0}), "protoss": defaultdict(lambda: {'replays': [], 'percent': 0}), "terran": defaultdict(lambda: {'replays': [], 'percent': 0})}

    def totalGames(self):
        return self.zergGames + self.protossGames + self.terranGames
    
    def buildUsageStats(self):
        for race in ['zerg', 'terran', 'protoss']:
            for k,v in self.buildOrders[race].items():
                self.buildOrders[race][k]['percent'] = len(v['replays']) / self.totalGames() * 100

            for k,v in self.buildOrders[race].items():
                print("~~~~~~~~~~~~~~~~~~~")
                print(k)
                print("percent used: "+str(v['percent']) + "%")
                for replay in v['replays']:
                    print(replay)