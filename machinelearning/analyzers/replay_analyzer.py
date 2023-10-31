import subprocess
import os
import json

import csv
from zerg_analyzer import ZergAnalyzer
from terran_analyzer import TerranAnalyzer
from protoss_analyzer import ProtossAnalyzer

zergAnalyzer = ZergAnalyzer()
terranAnalyzer = TerranAnalyzer()
protossAnalyzer = ProtossAnalyzer()

def getPlayerBuildOrder(playerID, cmds):
    buildOrder = []
    for cmd in cmds:
        if int(cmd['Frame']) > 7143:
            break
        if cmd['Type']['Name'] == 'Build' or cmd['Type']['Name'] == 'Train' or cmd['Type']['Name'] == 'Unit Morph' or cmd['Type']['Name'] == 'Building Morph' or cmd['Type']['Name'] == 'Upgrade':
            if cmd['PlayerID'] == playerID:
                if cmd['Type']['Name'] == 'Upgrade':
                    buildOrder.append({'frame': cmd['Frame'], 'command': cmd['Upgrade']['Name']})
                else:
                    buildOrder.append({'frame': cmd['Frame'], 'command': cmd['Unit']['Name']})

    buildOrder.sort(key=lambda x: x['frame'])
    return buildOrder

def analyzeReplays():

    FNULL = open(os.devnull, 'w')    #use this if you want to suppress output to stdout from the subprocess
    playerName = ""
    for filename in os.listdir('./DownloadedReplays'):
        path = "./DownloadedReplays/" + filename

        output = subprocess.run(["screp.exe", "-cmds", path], capture_output=True)

        output_dict = json.loads(output.stdout)

        cmds = output_dict['Commands']['Cmds']
        headers = output_dict['Header']

        currentReplayPlayers = {}

        for player in headers['Players']:
            playerName = player['Name']
            currentReplayPlayers[player['Name']] = {'playerName': player['Name'], 'teamID': player['Team'], 'race': player['Race']['Name'],'buildOrder': getPlayerBuildOrder(player['ID'], cmds)}

        for player,value in currentReplayPlayers.items():
            playerName = player
            race = value['race']
            buildOrder = value['buildOrder']
            
            if race == 'Zerg':
                zergAnalyzer.getBuildOrderRow(filename, playerName,  buildOrder)
            elif race == 'Terran':
                terranAnalyzer.getBuildOrderRow(filename, playerName,  buildOrder)
            elif race == 'Protoss':
                protossAnalyzer.getBuildOrderRow(filename, playerName,  buildOrder)
    
    zergAnalyzer.writeToCsv()
    terranAnalyzer.writeToCsv()
    protossAnalyzer.writeToCsv()

def getUnclassifiedReplays():
    
    zergAnalyzer.getUnclassifiedReplays()
    terranAnalyzer.getUnclassifiedReplays()
    protossAnalyzer.getUnclassifiedReplays()

if __name__=="__main__":
    analyzeReplays()
    getUnclassifiedReplays()
    
    