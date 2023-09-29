from .util import *

def classifyBuildOrder(root, buildOrder):
    for i, cmd in enumerate(buildOrder):
        for edge in root.edges:
            if withinTimeWindow(cmd['frame'], edge.logicalTimeFrame):
                return classifyBuildOrder(edge.dst, buildOrder[i+1:])
            
    return root.name