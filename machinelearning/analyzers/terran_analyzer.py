from base_analyzer import BaseAnalyzer
from models.terran_csv import terran_columns, TerranCSV

class TerranAnalyzer(BaseAnalyzer):
    def __init__(self):
        self.csv = TerranCSV()
        self.csv_filename = 'terran_all_replays' 
        self.columns = terran_columns

    def getBuildOrderRow(self, csv, filename, playerName, buildOrder):
        for command in buildOrder:
            newCommand = command['command']
            if newCommand in csv.columns:
                if self.csv.data[filename][playerName][newCommand] == -1:
                    self.csv.data[filename][playerName][newCommand] = command['frame']
                else:
                    for i in range(1, 5):
                        if command['command'] + " " + str(i) in csv.data[filename][playerName].keys():
                            if self.csv.data[filename][playerName][command['command'] + " " + str(i)] == -1:
                                self.csv.data[filename][playerName][command['command'] + " " + str(i)] = command['frame']
                                break

