from base_analyzer import BaseAnalyzer
from models.zerg_csv import ZergCSV

class ZergAnalyzer(BaseAnalyzer):
    def __init__(self):
        self.csv = ZergCSV()
        self.race = "zerg"
        self.csv_filename = f'{self.race}_all_replays.csv' 

    def getBuildOrderRow(self, filename, playerName, buildOrder):
        for command in buildOrder:
            newCommand = command['command']
            if newCommand == 'Hatchery':
                newCommand = 'Hatchery 1'
            if newCommand in self.csv.columns:
                if self.csv.data[filename][playerName][newCommand] == -1:
                    self.csv.data[filename][playerName][newCommand] = command['frame']
                else:
                    for i in range(1, 5):
                        if command['command'] + " " + str(i) in self.csv.data[filename][playerName].keys():
                            if self.csv.data[filename][playerName][command['command'] + " " + str(i)] == -1:
                                self.csv.data[filename][playerName][command['command'] + " " + str(i)] = command['frame']
                                break