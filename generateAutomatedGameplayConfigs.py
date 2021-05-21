# 
#

import glob
import json
import os
import sys

from jsonDataMethods import *

def generateMemberConfig(game, level, experimentId, enabledBehaviours, memberDescription):
    configFileName = game+"_"+experimentId+"_"+str(memberDescription["cellX"])+"_"+str(memberDescription["cellY"])+".json"
    configObject = {
        "game": game,
        "level": level,
        "behaviours": enabledBehaviours,
        "weights": memberDescription["weights"],
        "experimentId": experimentId
    }

    with open(configFileName, 'w') as newConfigFile:
        json.dump(configObject, newConfigFile)

def generateTeamAutomatedGameplayConfig(resultsJsonFile):
    with open(resultsJsonFile) as json_file:
        data = json.load(json_file)

    # experimentId
    experimentId = getExperimentId(data)
    print("Experiment ID: "+experimentId)

    # Game and level info
    gameLabel = getGame(data)
    levelId = getLevelId(data)
    print("Game: "+gameLabel + " level: "+str(levelId))

    # Enabled behaviours
    enabledBehaviours = getEnabledBehaviours(data)

    # Get description of the agents generated and occupying the MAP-ELites
    teamData = getMAPElitesMembersDescription(data["result"])
    print(teamData)

    # Generate config files for each team member
    print("Generate config files for each member of the team")
    for member in teamData:
        generateMemberConfig(gameLabel, levelId, experimentId, enabledBehaviours, member)
    return
   
folderPath = sys.argv[1]

for filename in glob.glob(os.path.join(folderPath, '*.json')):
    print("Processing "+filename)
    generateTeamAutomatedGameplayConfig(filename)
    print("")
