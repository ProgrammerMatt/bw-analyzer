import json
from .util import *
 
class Node:
    #Buildings/Units
    def __init__(self, name='Unidentified', edges=[]):
        self.edges = []
        for child in edges:
            self.edges.append(child)
        self.name = name

    def __str__(self):
        return self.name

class Edge:
    #Logical Frames
    def __init__(self, gameTimeStamp, command=None, src=None, dst=None):
        self.timestamp = gameTimeStamp
        self.logicalTimeFrame = getLogicalFrameFromTime(int(gameTimeStamp))
        self.command = command
        self.src = src
        self.dst = dst

    def __str__(self):
        return str(self.logicalTimeFrame) + " -> " + self.command

def buildTree(root, data):
    if not data:
        return
    
    for timestamp,cmdsList in data.items():
        for cmd in cmdsList:
            cmdItem = list(cmd.keys())[0]
            buildOrderName = cmd[cmdItem]
            newChild = Node(name=buildOrderName['build'])
            newEdge = Edge(gameTimeStamp=timestamp, command=cmdItem, src=root, dst=newChild)
            root.edges.append(newEdge)
            temp = {key: buildOrderName[key] for key in filter(lambda x: x.isdigit(), buildOrderName.keys())}
            buildTree(newChild, temp)  
                

def buildTrees():
    trees = {"zerg": Node(), "protoss": Node(), "terran": Node()}
    
    #for race in trees.keys():
    for race in ['zerg']: 
        f = open("classifier_trees/"+race+".json")
        data = json.load(f)
        buildTree(trees[race], data)
        f.close()

    return trees