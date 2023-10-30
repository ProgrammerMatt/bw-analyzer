import subprocess
import os
import json

from classifiers.base_classifier import *
from classifiers.treebuilder import buildTrees

from collections import defaultdict
from models.player import Player

from models.zerg_csv import *
from models.terran_csv import *
import csv
from zerg_analyzer import ZergAnalyzer
from terran_analyzer import TerranAnalyzer

zergAnalyzer = ZergAnalyzer()
terranAnalyzer = TerranAnalyzer()

def getPlayerBuildOrder(playerID, cmds):
    buildOrder = []
    for cmd in cmds: 
        if cmd['Type']['Name'] == 'Build' or cmd['Type']['Name'] == 'Train' or cmd['Type']['Name'] == 'Unit Morph' or cmd['Type']['Name'] == 'Building Morph' or cmd['Type']['Name'] == 'Upgrade':
            if cmd['PlayerID'] == playerID:
                if cmd['Type']['Name'] == 'Upgrade':
                    buildOrder.append({'frame': cmd['Frame'], 'command': cmd['Upgrade']['Name']})
                else:
                    buildOrder.append({'frame': cmd['Frame'], 'command': cmd['Unit']['Name']})

    buildOrder.sort(key=lambda x: x['frame'])
    return buildOrder

def getTerranBuildOrderRow(csv, filename, playerName, buildOrder):
    for command in buildOrder:
        newCommand = command['command']
        if newCommand == 'Hatchery':
            newCommand = 'Hatchery 1'
        if newCommand in csv.columns:
            if csv.data[filename][playerName][newCommand] == -1:
                csv.data[filename][playerName][newCommand] = command['frame']
            else:
                for i in range(1, 5):
                    if command['command'] + " " + str(i) in csv.data[filename][playerName].keys():
                        if csv.data[filename][playerName][command['command'] + " " + str(i)] == -1:
                            csv.data[filename][playerName][command['command'] + " " + str(i)] = command['frame']
                            break


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
            if race == 'Terran':
                terranAnalyzer.getBuildOrderRow(filename, playerName,  buildOrder)
    
    zergAnalyzer.writeToCsv()
    terranAnalyzer.writeToCsv()

def getUnclassifiedReplays():
    
    with open('zerg_classified.csv', encoding="utf-8", newline='') as classified_csv:
        with open('zerg_all_replays.csv', encoding="utf-8", newline='') as all_replays_csv:
            classified_reader = csv.reader(classified_csv, delimiter=',', quotechar='|')
            classifiedReplays = []
            for classified_row in classified_reader:
                classifiedReplays.append(classified_row[0:2])

            all_reader = csv.reader(all_replays_csv, delimiter=',', quotechar='|')
            with open('zerg_unclassified.csv', 'w', encoding="utf-8", newline='') as unclassified_csv:
                writer = csv.writer(unclassified_csv, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                from models.zerg_csv import zerg_columns
                writer.writerow(["file", "player", "build"] + zerg_columns)
                for all_row in all_reader:
                    if [all_row[0],all_row[1]] not in classifiedReplays:
                        writer.writerow(all_row)
                else: 
                    print(f"{all_row[0]} - {all_row[1]}")

if __name__=="__main__":
    #analyzeReplays()
    getUnclassifiedReplays()
    
    