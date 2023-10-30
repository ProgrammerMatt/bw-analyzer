from collections import defaultdict

terran_columns = [
            "Supply Depot 1",
            "Barracks",
            "Refinery",
            "Barracks",
            "Supply Depot 2"
            "Factory 1",
            "Factory 2",
            "Factory 3",
            "Armory",
            "Academy",
            "Engineering Bay"
        ]

class TerranCSV:
    def __init__(self):

        self.columns = [
            "Supply Depot 1",
            "Barracks",
            "Refinery",
            "Barracks",
            "Supply Depot 2"
            "Factory 1",
            "Factory 2",
            "Factory 3",
            "Armory",
            "Academy",
            "Engineering Bay"
        ]

        self.race = 'terran'
        
        self.data = defaultdict(lambda: defaultdict(lambda: {col: -1 for col in self.columns}))
