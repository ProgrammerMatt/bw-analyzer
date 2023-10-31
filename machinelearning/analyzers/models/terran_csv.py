from collections import defaultdict

class TerranCSV:
    def __init__(self):

        self.columns = [
            "Supply Depot 1",
            "Supply Depot 2",
            "Supply Depot 3",
            "Supply Depot 4",
            "Supply Depot 5",
            "Barracks 1",
            "Barracks 2",
            "Barracks 3",
            "Barracks 4",
            "Barracks 5",
            "Refinery 1",
            "Refinery 2",
            "Factory 1",
            "Factory 2",
            "Factory 3",
            "Factory 4",
            "Factory 5",
            "Armory",
            "Academy",
            "Engineering Bay",
            "Command Center 1",
            "Command Center 2"
        ]

        self.race = 'terran'
        
        self.data = defaultdict(lambda: defaultdict(lambda: {col: -1 for col in self.columns}))
