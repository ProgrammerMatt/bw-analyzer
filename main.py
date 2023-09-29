import subprocess
import os
import json

from classifiers.base_classifier import *
from classifiers.treebuilder import buildTrees

trees = buildTrees()

def getPlayerBuildOrder(playerID):
    buildOrder = []
    for cmd in cmds: 
        if cmd['Type']['Name'] == 'Build' or cmd['Type']['Name'] == 'Train' or cmd['Type']['Name'] == 'Unit Morph':
            if cmd['PlayerID'] == playerID:
                buildOrder.append({'frame': cmd['Frame'], 'command': cmd['Unit']['Name']})

    buildOrder.sort(key=lambda x: x['frame'])
    return buildOrder

FNULL = open(os.devnull, 'w')    #use this if you want to suppress output to stdout from the subprocess
filename = "C:/Users/Matt/Downloads/QYfqmjkuls66t-_c5DXneSXjxcULAQf5mHaYLsU6wwA.rep"

output = subprocess.run(["screp.exe", "-cmds", filename], capture_output=True)

output_dict = json.loads(output.stdout)
json_object = json.dumps(output_dict, indent=4)

cmds = output_dict['Commands']['Cmds']
headers = output_dict['Header']

players = {}


for player in headers['Players']:
    players[player['Name']] = {'playerName': player['Name'], 'teamID': player['Team'], 'race': player['Race']['Name'],'buildOrder': getPlayerBuildOrder(player['ID'])}




for player,value in players.items():
    race = value['race']
    buildOrder = value['buildOrder']
    if race == 'Zerg':
        classifiedBuildOrder = classifyBuildOrder(trees['zerg'], buildOrder)
    if race == 'Protoss':
        classifiedBuildOrder = classifyBuildOrder(trees['protoss'], buildOrder)
    if race == 'Terran':
        classifiedBuildOrder = classifyBuildOrder(trees['terran'], buildOrder)

    print(player + " used: "+classifiedBuildOrder)





    