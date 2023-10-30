from base_analyzer import BaseAnalyzer
from models.zerg_csv import zerg_columns, ZergCSV

class ZergAnalyzer(BaseAnalyzer):
    def __init__(self):
        self.csv = ZergCSV()
        self.csv_filename = 'zerg_all_replays' 
        self.columns = zerg_columns

    def getBuildOrderRow(self, csv, filename, playerName, buildOrder):
        for command in buildOrder:
            newCommand = command['command']
            if newCommand == 'Hatchery':
                newCommand = 'Hatchery 1'
            if newCommand in csv.columns:
                if self.csv.data[filename][playerName][newCommand] == -1:
                    self.csv.data[filename][playerName][newCommand] = command['frame']
                else:
                    for i in range(1, 5):
                        if command['command'] + " " + str(i) in csv.data[filename][playerName].keys():
                            if self.csv.data[filename][playerName][command['command'] + " " + str(i)] == -1:
                                self.csv.data[filename][playerName][command['command'] + " " + str(i)] = command['frame']
                                break

