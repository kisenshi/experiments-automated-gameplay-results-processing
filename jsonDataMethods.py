# Read JSON file

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

def getGameRuns(data):
    return data['config']['frameworkConfig']['nGameRuns']

def getMapIterations(data):
    return data['config']['mapElitesConfig']['nMapElitesIterations']

def getMAPElitesMatrix(sizeX, sizeY, data):
    matrix = [[None for i in range(sizeX)] for i in range(sizeY)]
    mapElites = data['mapElites']

    for agentData in data['occupiedCellsIdx']:
        x = agentData['x']
        y = agentData['y']
        matrix[y][x] = (mapElites[x][y]['performance'])*(-1)

    print(DataFrame(matrix))

    return matrix, len(data['occupiedCellsIdx'])