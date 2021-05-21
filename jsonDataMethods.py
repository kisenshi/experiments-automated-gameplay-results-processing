# Parse and return certain elements of the JSON file generated from the 
# execution of the MAP-Elites that generates a team of agents for a pair of 
# features. This JSON contains the MAP-ELites but also information about the
# experiment carried out to generate it. 

from pandas import *

# GET DATA FROM JSON
def getExperimentId(data):
    return data['config']['experimentId']

def featuresInfo(data):
    featureDetails = data['featuresDetails']

    featureX = data['config']['mapElitesConfig']['featureX']
    featureY = data['config']['mapElitesConfig']['featureY']

    return featureX, featureY

def performanceInfo(data):
    return data['config']['mapElitesConfig']['performanceCriteria']


def getFeatureLabels(feature, data):
    return data['featuresDetails'][feature]['bucketsRangeInfo']

def getGame(data):
    return data['config']['frameworkConfig']['game']

def getLevelId(data):
    return data['config']['frameworkConfig']['level']

def getGameRuns(data):
    return data['config']['frameworkConfig']['nGameRuns']

def getMapIterations(data):
    return data['config']['mapElitesConfig']['nMapElitesIterations']

def getEnabledBehaviours(data):
    return data['teamInfo']['enabledBehaviours']

def getMAPElitesMatrix(sizeX, sizeY, data):
    matrix = [[None for i in range(sizeX)] for i in range(sizeY)]
    mapElites = data['mapElites']

    for agentData in data['occupiedCellsIdx']:
        x = agentData['x']
        y = agentData['y']
        matrix[y][x] = (mapElites[x][y]['performance'])*(-1)

    print(DataFrame(matrix))

    return matrix, len(data['occupiedCellsIdx'])

def getMAPElitesMembersDescription(data):
    teamData = []
    mapElites = data['mapElites']

    for agentData in data['occupiedCellsIdx']:
        x = agentData['x']
        y = agentData['y']
        agentDescription = {
            "cellX": agentData['x'],
            "cellY": agentData['y'],
            "weights": mapElites[x][y]["heuristicsWeightList"]
        }
        teamData.append(agentDescription)

    return teamData