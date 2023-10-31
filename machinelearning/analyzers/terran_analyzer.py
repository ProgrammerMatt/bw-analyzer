from base_analyzer import BaseAnalyzer
from models.terran_csv import TerranCSV

class TerranAnalyzer(BaseAnalyzer):
    def __init__(self):
        self.csv = TerranCSV()
        self.race = "terran"
        self.csv_filename = f'{self.race}_all_replays.csv'

    def getBuildOrderRow(self, filename, playerName, buildOrder):
        for command in buildOrder:
            for i in range(1, 6):
                if command['command'] + " " + str(i) in self.csv.data[filename][playerName].keys():
                    if self.csv.data[filename][playerName][command['command'] + " " + str(i)] == -1:
                        self.csv.data[filename][playerName][command['command'] + " " + str(i)] = command['frame']
                        break


