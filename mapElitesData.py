# Parse the MAP-Elites resulting json that contains a team of agents and 
# generates a graph of the corresponding heatmap, as an image. Refer to the work 
# presented in "MAP-Elites to Generate a Team of Agents that Elicits Diverse 
# Automated Gameplay" for more information.
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
import os
import glob

import json
import numpy

import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go

from IPython.display import Image

from jsonDataMethods import *

def generateMAPElitesHeatmap(matrix, featureX, featureY, featureXLabels, featureYLabels, performanceLabel, gameLabel, nAgents):
    plotlyExpress(matrix, featureX, featureY, featureXLabels, featureYLabels, performanceLabel, gameLabel, nAgents)

def plotlyGraph(matrix, xInfo, yInfo, xLabels, yLabels, colorLabel, title):
    fig = go.Figure(
        data=go.Heatmap(
            z=matrix,
            x=xLabels,
            y=yLabels,
            hoverongaps=False,
            colorscale='RdYlGn_r',
            #colorscale='rainbow_r',
            #colorscale='speed_r',
            #name=performanceLabel,
        )
    )

    axis_template = dict(
        showgrid=False, 
        zeroline=False
    )

    fig.update_layout(
        xaxis=axis_template,
        yaxis=axis_template,
        title=title,
        xaxis_title=xInfo,
        yaxis_title=yInfo,
    )

    fig.show()
    fig.write_image("test.png")

def plotlyExpress(data, xInfo, yInfo, xLabels, yLabels, colorLabel, gameLabel, nAgents):
    title = gameLabel + ": " + str(nAgents) + " ELITES"

    labels = dict(
        x=xInfo, 
        y=yInfo, 
        color="game over ts"
    )

    fig = px.imshow(data,
        labels=labels,
        x=xLabels,
        y=yLabels,
        color_continuous_scale='RdYlGn_r',
    )

    axis_template = dict(
        showgrid=False, 
        zeroline=False
    )

    fig.update_layout(
        xaxis=axis_template,
        yaxis=axis_template,
        title=title,
    )

    #fig.update_xaxes(side="top")
    fig.update_yaxes(autorange=True) 
    
    filename=gameLabel+'_'+xInfo+'_'+yInfo+'.png'

    print("Exporting to "+filename)
    fig.write_image(filename)

    #pio.write_image(fig, filename+'1.png')
    #fig.show()
    #fig.write_image("fig1.svg")
    #displayGraph(fig)
    #fig.write_image(title+"_"+xInfo+"_"+yInfo+".svg", width=1500)

def generateMAPElitesImage(resultsJsonFile):
    with open(resultsJsonFile) as json_file:
        data = json.load(json_file)

    # Game info
    gameLabel = getGame(data)
    print("Game: "+gameLabel)

    # Features and performance info
    featureX, featureY = featuresInfo(data)
    featureXLabels = getFeatureLabels(featureX, data)
    featureYLabels = getFeatureLabels(featureY, data)

    performanceLabel = performanceInfo(data)

    print("X: "+ featureX)
    print("Y: "+featureY)

    # matrix data
    matrix, nAgents = getMAPElitesMatrix(len(featureXLabels), len(featureYLabels), data["result"])

    # Generate heatmap
    generateMAPElitesHeatmap(matrix, featureX, featureY, featureXLabels, featureYLabels, performanceLabel, gameLabel, nAgents)

def generateMAPElitesImageFromTemp(generalInfoJson, resultsJson):
    # Game info
    gameLabel = getGame(generalInfoJson)
    print("Game: "+gameLabel)

    # Features and performance info
    featureX, featureY = featuresInfo(generalInfoJson)
    featureXLabels = getFeatureLabels(featureX, generalInfoJson)
    featureYLabels = getFeatureLabels(featureY, generalInfoJson)

    performanceLabel = performanceInfo(generalInfoJson)

    print("X: "+ featureX)
    print("Y: "+featureY)

    # matrix data
    matrix, nAgents = getMAPElitesMatrix(len(featureXLabels), len(featureYLabels), resultsJson["resultTemp"])

    # Generate heatmap
    iteration=resultsJson['iteration']
    gameLabel=gameLabel+" it. "+str(iteration)
    generateMAPElitesHeatmap(matrix, featureX, featureY, featureXLabels, featureYLabels, performanceLabel, gameLabel, nAgents)


folderPath = sys.argv[1]

if len(sys.argv) > 2:
    tempN = sys.argv[2]

    generalInfoFile = folderPath+"/MapElitesGameplay_temp_general_info.json"
    tempResults = folderPath+"/MapElitesGameplay_temp_"+tempN+".json"

    print("Processing "+generalInfoFile+" "+tempResults)
    
    with open(generalInfoFile) as json_file:
        generalInfoJson = json.load(json_file)
    
    with open(tempResults) as json_file:
        resultsJson = json.load(json_file)

    generateMAPElitesImageFromTemp(generalInfoJson, resultsJson)
else :
    for filename in glob.glob(os.path.join(folderPath, '*.json')):
        print("Processing "+filename)
        generateMAPElitesImage(filename)
        print("")