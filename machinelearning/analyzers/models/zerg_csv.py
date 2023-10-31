from collections import defaultdict

class ZergCSV:
    def __init__(self):

        self.columns = [
            "Spawning Pool",
            "Extractor",
            "Hatchery 1",
            "Hatchery 2",
            "Lair",
            "Spire",
            "Metabolic Boost (Zergling Speed)"
        ]

        self.race = 'zerg'
        
        self.data = defaultdict(lambda: defaultdict(lambda: {col: -1 for col in self.columns}))
