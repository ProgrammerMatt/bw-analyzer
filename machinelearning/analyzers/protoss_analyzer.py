from base_analyzer import BaseAnalyzer
from models.protoss_csv import ProtossCSV

class ProtossAnalyzer(BaseAnalyzer):
    def __init__(self):
        self.csv = ProtossCSV()
        self.race = "protoss"
        self.csv_filename = f'{self.race}_all_replays.csv'

    def getBuildOrderRow(self, filename, playerName, buildOrder):
        for command in buildOrder:
            for i in range(1, 6):
                if command['command'] + " " + str(i) in self.csv.data[filename][playerName].keys():
                    if self.csv.data[filename][playerName][command['command'] + " " + str(i)] == -1:
                        self.csv.data[filename][playerName][command['command'] + " " + str(i)] = command['frame']
                        break


