# The MAP-Elites automated gameplay algorithm generates a series of temporary
# json during its execution. This code merges the two temporary files 
# MapElitesGameplay_temp_general_info.json and MapElitesGameplay_temp_TEMPN.json 
# into a unique one. This final json is similar in structure and name to the one
# generated when the MAP-ELites algorithm has finished, so it can be parsed as
# that one. Refer to the work presented in "MAP-Elites to Generate a Team of Agents 
# that Elicits Diverse Automated Gameplay" for more information.
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

import sys
import json
from jsonDataMethods import *

folderPath = sys.argv[1]
tempN = sys.argv[2]

generalInfoFile = folderPath+"/MapElitesGameplay_temp_general_info.json"
tempResults = folderPath+"/MapElitesGameplay_temp_"+tempN+".json"

print("Merging "+generalInfoFile+" and "+tempResults)
    
with open(generalInfoFile) as json_file:
    generalInfoJson = json.load(json_file)
    
with open(tempResults) as json_file:
    resultsTempJson = json.load(json_file)

resultsTempJson['result'] = resultsTempJson.pop('resultTemp')
generalInfoJson.update(resultsTempJson)

experimentId = getExperimentId(generalInfoJson)
gameName = getGame(generalInfoJson).lower()
featureX, featureY = featuresInfo(generalInfoJson)
performance = performanceInfo(generalInfoJson)
gameRuns = str(getGameRuns(generalInfoJson))
mapIterations = str(getMapIterations(generalInfoJson))

finalFileName = "MAPElitesGameplay_"+experimentId+"_"+gameName+"_x_"+featureX+"_y_"+featureY+"_perf_"+performance+"_"+gameRuns+"_"+mapIterations+".json"
print("Creating "+finalFileName)

with open(finalFileName, 'w') as newFile:
    json.dump(generalInfoJson, newFile)