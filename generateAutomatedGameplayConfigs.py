# Generate config files for each of the team members generated from the
# experiments presented in "MAP-Elites to Generate a Team of Agents that Elicits 
# Diverse Automated Gameplay". Parse the final resulting json containing the
# information about the experiments and resulting MAP-Elites and agents 
# description and generates individual json config files for each of them.
# These config files are meant to be used in the automatedGameplay standalone
# to trigger and run each agent.
#
# Copyright (C) 2021 Cristina Guerrero-Romero
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
