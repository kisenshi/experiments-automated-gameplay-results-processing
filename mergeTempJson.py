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