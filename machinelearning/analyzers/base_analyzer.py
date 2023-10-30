from abc import ABC, abstractmethod

class BaseAnalyzer(ABC):

    csv = None
    csv_filename = None
    columns = None
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def getBuildOrderRow(self, csv, filename, playerName, buildOrder):
        pass

    def writeToCsv(self):
        with open(self.csv_filename, 'w', encoding="utf-8", newline='') as csvfile:
            writer = self.csv.writer(csvfile, delimiter=',',
                                    quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["file", "player", "build"] +self.columns)
            
            for rep in self.csv.data.keys():
                for player in self.csv.data[rep].keys():
                    writer.writerow([rep, player, ''] + [val for val in self.csv.data[rep][player].values()][3:])