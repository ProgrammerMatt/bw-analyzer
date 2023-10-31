from abc import ABC, abstractmethod
import csv

class BaseAnalyzer(ABC):

    csv = None
    csv_filename = None
    race = None
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def getBuildOrderRow(self, csv, filename, playerName, buildOrder):
        pass

    def writeToCsv(self):
        with open(self.csv_filename, 'w', encoding="utf-8", newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',
                                    quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["file", "player", "build"] +self.csv.columns)
            
            for rep in self.csv.data.keys():
                for player in self.csv.data[rep].keys():
                    writer.writerow([rep, player, ''] + [val for val in self.csv.data[rep][player].values()])

    
    def getUnclassifiedReplays(self):
        
        with open(f'{self.race}_classified.csv', encoding="utf-8", newline='') as classified_csv:
            with open(f'{self.race}_all_replays.csv', encoding="utf-8", newline='') as all_replays_csv:
                classified_reader = csv.reader(classified_csv, delimiter=',', quotechar='|')
                classifiedReplays = []
                for classified_row in classified_reader:
                    classifiedReplays.append(classified_row[0:2])

                all_reader = csv.reader(all_replays_csv, delimiter=',', quotechar='|')
                with open(f'{self.race}_unclassified.csv', 'w', encoding="utf-8", newline='') as unclassified_csv:
                    writer = csv.writer(unclassified_csv, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow(["file", "player", "build"] + self.csv.columns)
                    for all_row in all_reader:
                        if [all_row[0],all_row[1]] not in classifiedReplays:
                            writer.writerow(all_row)
                    else: 
                        print(f"{all_row[0]} - {all_row[1]}")