from collections import defaultdict

class ProtossCSV:
    def __init__(self):

        self.columns = [
            "Pylon 1",
            "Pylon 2",
            "Pylon 3",
            "Pylon 4",
            "Pylon 5",
            "Gateway 1",
            "Gateway 2",
            "Gateway 3",
            "Gateway 4",
            "Gateway 5",
            "Assimilator 1",
            "Assimilator 2",
            "Stargate 1",
            "Stargate 2",
            "Stargate 3",
            "Stargate 4",
            "Stargate 5",
            "Forge 1",
            "Citadel of Adun",
            "Robotics Facility",
            "Templar Archives",
            "Robotics Support Bay",
            "Photon Cannon 1",
            "Photon Cannon 2",
            "Photon Cannon 3",
            "Photon Cannon 4",
            "Photon Cannon 5",
            "Observatory",
            "Fleet Beacon",
            "Arbiter Tribunal",
            "Nexus 1",
            "Nexus 2"
        ]

        self.race = 'protoss'
        
        self.data = defaultdict(lambda: defaultdict(lambda: {col: -1 for col in self.columns}))
