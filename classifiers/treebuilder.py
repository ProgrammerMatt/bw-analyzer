import json
 
class Node:
    #Buildings/Units
    def __init__(self, name='root', edges=[]):
        self.edges = []
        for child in edges:
            self.edges.append(child)
        self.name = name

    def __str__(self):
        return self.name

class Edge:
    #Logical Frames
    def __init__(self, logicalTimeFrame, src=None, dst=None):
        self.logicalTimeFrame = logicalTimeFrame
        self.src = src
        self.dst = dst

    def __str__(self):
        return self.logicalTimeFrame

def buildTree(root, data):
    if not data:
        return
    
    for key,value in data.items():
            for each in value.keys():
                newChild = Node(each)
                newEdge = Edge(logicalTimeFrame=int(key), src=root, dst=newChild)
                root.edges.append(newEdge)
                buildTree(newChild, value[each])  
                

def buildTrees():
    trees = {"zerg": Node(), "protoss": Node(), "terran": Node()}
    
    for race in trees.keys():
        f = open("classifier_trees/"+race+".json")
        data = json.load(f)
        buildTree(trees[race], data)
        f.close()

    return trees