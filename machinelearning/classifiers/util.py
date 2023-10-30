def getLogicalFrameFromTime(timestampInSeconds):
    return timestampInSeconds * 23.81

def getTimeFromLogicalFrame(logicalFrame):
    return logicalFrame // 23.81

def withinTimeWindow(logicalFrameStandard, logicalFrameToCheck):
    return logicalFrameToCheck > logicalFrameStandard - 150 and logicalFrameToCheck < logicalFrameStandard + 150