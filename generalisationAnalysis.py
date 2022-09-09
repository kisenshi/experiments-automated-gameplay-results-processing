# Scripts to create graphs with information about the distribution of the stats
# in each of the levels.
#
# Copyright (C) 2022 Cristina Guerrero Romero
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
import pylab
import plotly.graph_objects as go
import plotly.io as pio

N_RESULTS = 100
N_PORTABILITY_LEVELS = 5
N_TOTAL_LEVELS = 6

#GRAPHS_PATH = "test/"
GRAPHS_PATH = "results_portability_broken/"

# GAMES
B3 = "B3"

# DIMENSIONS
SCORE = "Score"
CURIOSITY = "Curiosity"
COLLISIONS = "Collisions"
WIN_RATE = "Victories"
EOG = "EoG"
EXPLORATION = "Exploration"

# Butterflies
LEVELS_THESIS_IDS = [
    "7.2a",
    "7.19a",
    "7.19b",
    "7.19c",
    "7.19d",
    "`Broken`"
]

B3_RESULTS = "generalisation/results_B3/"

B3_E1_RECORDBREAKER = B3_RESULTS+"E1/B3_E1_record_breaker.txt"
B3_E2_RECORDBREAKER = B3_RESULTS+"E2/B3_E2_record_breaker.txt"
B3_E3_CURIOUS       = B3_RESULTS+"E3/B3_E3_curious.txt"
B3_E4_GAME          = B3_RESULTS+"E4/B3_E4_game.txt"
B3_E4_WINNER        = B3_RESULTS+"E4/B3_E4_winner.txt"
B3_E5_EXPLORER      = B3_RESULTS+"E5/B3_E5_explorer.txt"
B3_E6_CURIOUS       = B3_RESULTS+"E6/B3_E6_curious.txt"
B3_E6_EXPLORER      = B3_RESULTS+"E6/B3_E6_explorer.txt"

class PlotInfo:
    def __init__(self, title, img_title, yaxis_range=None):
        self.title = title
        self.img_title = img_title
        self.yaxis_range = yaxis_range

def printList(data):
    info = ""
    for x in range(len(data)):
        info += str(data[x]) + ", "
    return info

def getFileResultsData(file_name):
	print("Reading "+file_name)

	files = glob.glob(file_name)
	if len(files) == 0:
		print("Missing file: ", file_name)
		return None

	return pylab.loadtxt(files[0], comments='*', delimiter=' ', usecols=range(3))

def getFileResultsDataInOneRow(file_name):
	print("Reading "+file_name+" All data is in a row")

	files = glob.glob(file_name)
	if len(files) == 0:
		print("Missing file: ", file_name)
		return None

	return pylab.loadtxt(files[0], comments='*', delimiter=' ')

# Method used for testing 1
def OnePlotPortability(data, loadDimensionData, dimension_name, agent_name):
    fig = go.Figure()

    # For portability, we do not include the result of the broken level
    for lvl in range(0, N_PORTABILITY_LEVELS):
        first_result = N_RESULTS * lvl
        last_result = N_RESULTS + first_result

        data_title = "Level " + str(lvl)
        graph_data = loadDimensionData(data, first_result, last_result)
        print(dimension_name + " " + data_title + ": "+ printList(graph_data))

        fig.add_trace(go.Box(
            y=graph_data,
            name=data_title
        ))

    fig.update_layout(
        title="Resulting stats "+agent_name,
        yaxis_title=dimension_name,
        showlegend=True,
        yaxis_range=None
    )

    fig.show()

# Method used for testing 2
def TwoPlotsPortability(data1, data2, loadDimensionData, dimension_name, agent_name1, agent_name2):
    fig = go.Figure()

    # For portability, we do not include the result of the broken level
    # Populate level information for each agent
    levels_info = []
    agent1_levels_data = []
    agent2_levels_data = []
    for lvl in range(0, N_PORTABILITY_LEVELS):
        first_result = N_RESULTS * lvl
        last_result = N_RESULTS + first_result

        #level = "Level " + str(lvl)
        level = LEVELS_THESIS_IDS[lvl]
        level_data_size = last_result-first_result
        level_info = [level for i in range(level_data_size)]
        levels_info.extend(level_info)

        # Agents data for current level
        graph_data1 = loadDimensionData(data1, first_result, last_result)
        agent1_levels_data.extend(graph_data1)

        graph_data2 = loadDimensionData(data2, first_result, last_result)
        agent2_levels_data.extend(graph_data2)

    print("Trace 1 y" + printList(agent1_levels_data))
    print("Trace 1 x" + printList(levels_info))
    fig.add_trace(go.Box(
        y=agent1_levels_data,
        x=levels_info,
        name=agent_name1
    ))

    print("Trace 2 y" + printList(agent2_levels_data))
    print("Trace 2 x" + printList(levels_info))
    fig.add_trace(go.Box(
        y=agent2_levels_data,
        x=levels_info,
        name=agent_name2
    ))

    fig.update_layout(
        title="Resulting stats",
        yaxis_title=dimension_name,
        showlegend=True,
        yaxis_range=None,
        boxmode='group'
    )

    fig.show()

def PlotsPortability(agents_data, loadDimensionData, dimension_name, agent_names, plot_info):
    fig = go.Figure()

    # For portability, we do not include the result of the broken level.
    # Populate level information for each agent.
    levels_info = []
    n_agents = len(agents_data)
    agent_levels_data = [[] for i in range(n_agents)]
    print("Debug: n_agents: "+ str(n_agents) + " agent_levels_data: "+printList(agent_levels_data))

    for lvl in range(0, N_PORTABILITY_LEVELS):
        first_result = N_RESULTS * lvl
        last_result = N_RESULTS + first_result

        #level = "Level " + str(lvl)
        level = LEVELS_THESIS_IDS[lvl]
        level_data_size = last_result-first_result
        level_info = [level for i in range(level_data_size)]
        levels_info.extend(level_info)

        # Agents data for current level.
        for i, data in enumerate(agents_data):
            graph_data = loadDimensionData(data, first_result, last_result)
            agent_levels_data[i].extend(graph_data)

    # Create plots for each agent so they are grouped.
    for i in range(0, n_agents):
        print("Trace "+ str(i) +" y" + printList(agent_levels_data[i]))
        print("Trace "+ str(i) +" x" + printList(levels_info))
        fig.add_trace(go.Box(
            y=agent_levels_data[i],
            x=levels_info,
            name=agent_names[i]
        ))

    fig.update_layout(
        title=plot_info.title,
        yaxis_title=dimension_name,
        showlegend=True,
        yaxis_range=plot_info.yaxis_range,
        boxmode='group'
    )

    fig.show()
    pio.write_image(fig, GRAPHS_PATH+plot_info.img_title, format='pdf')
    #pio.write_image(fig, GRAPHS_PATH+plot_info.img_title, format='pdf', width=1080)
    # pio.write_image(fig, GRAPHS_PATH+plot_info.img_title+"A", format='png', width=1080)
    # pio.write_image(fig, GRAPHS_PATH+plot_info.img_title+"B", format='png', scale=6, width=1080)
    #fig.write_image(GRAPHS_PATH+plot_info.img_title+".png")

# PlostsPortabilityAll extends PlotsPortability to add the broken level data if requested.
def PlotsPortabilityAll(agents_data, loadDimensionData, dimension_name, agent_names, plot_info, add_broken=False):
    fig = go.Figure()

    # For portability, we do not include the result of the broken level.
    # Populate level information for each agent.
    levels_info = []
    broken_level_info = []
    n_agents = len(agents_data)
    agent_levels_data = [[] for i in range(n_agents)]
    agent_broken_levels_data = [[] for i in range(n_agents)]

    for lvl in range(0, N_PORTABILITY_LEVELS):
        first_result = N_RESULTS * lvl
        last_result = N_RESULTS + first_result

        #level = "Level " + str(lvl)
        level = LEVELS_THESIS_IDS[lvl]
        level_data_size = last_result-first_result
        level_info = [level for i in range(level_data_size)]
        levels_info.extend(level_info)

        # Agents data for current level.
        for i, data in enumerate(agents_data):
            graph_data = loadDimensionData(data, first_result, last_result)
            agent_levels_data[i].extend(graph_data)

    # Create plots for each agent so they are grouped.
    for i in range(0, n_agents):
        print("Trace "+ str(i) +" y" + printList(agent_levels_data[i]))
        print("Trace "+ str(i) +" x" + printList(levels_info))
        fig.add_trace(go.Box(
            y=agent_levels_data[i],
            x=levels_info,
            name=agent_names[i]
        ))

    if(add_broken):
        # Add broken level
        lvl = N_PORTABILITY_LEVELS
        first_result = N_RESULTS * lvl
        last_result = N_RESULTS + first_result
        level_data_size = last_result-first_result
        broken_level_info = [LEVELS_THESIS_IDS[lvl] for i in range(level_data_size)]
        for i, data in enumerate(agents_data):
            graph_data = loadDimensionData(data, first_result, last_result)
            agent_broken_levels_data[i].extend(graph_data)
        
        for i in range(0, n_agents):
            print("`Broken` Trace "+ str(i) +" y" + printList(agent_broken_levels_data[i]))
            print("`Broken` Trace "+ str(i) +" x" + printList(broken_level_info))
            fig.add_trace(go.Box(
                y=agent_broken_levels_data[i],
                x=broken_level_info,
                name=agent_names[i]
            ))

    fig.update_layout(
        title=plot_info.title,
        yaxis_title=dimension_name,
        showlegend=True,
        yaxis_range=plot_info.yaxis_range,
        boxmode='group'
    )

    fig.show()
    pio.write_image(fig, GRAPHS_PATH+plot_info.img_title+".pdf", format='pdf')

# HistogramsPortabilityAll generates an histogram instead of a whisker plot.
def HistogramsPortabilityAll(agents_data, loadDimensionData, dimension_name, agent_names, plot_info, add_broken=False):
    fig = go.Figure()

    # For portability, we do not include the result of the broken level.
    # Populate level information for each agent.
    levels_info = []
    broken_level_info = []
    n_agents = len(agents_data)
    agent_levels_data = [[] for i in range(n_agents)]
    agent_broken_levels_data = [[] for i in range(n_agents)]

    for lvl in range(0, N_PORTABILITY_LEVELS):
        first_result = N_RESULTS * lvl
        last_result = N_RESULTS + first_result

        # Agents data for current level.
        for i, data in enumerate(agents_data):
            graph_data = loadDimensionData(data, first_result, last_result)
            agent_levels_data[i].extend(graph_data)
            # Not all data is populated in this case
            level_data_size = len(graph_data)
            level_info = [LEVELS_THESIS_IDS[lvl] for i in range(level_data_size)]
            levels_info.extend(level_info)

    # Create plots for each agent so they are grouped.
    for i in range(0, n_agents):
        print("Trace "+ str(i) +" y" + printList(agent_levels_data[i]))
        print("Trace "+ str(i) +" x" + printList(levels_info))
        fig.add_trace(go.Histogram(
            y=agent_levels_data[i],
            x=levels_info,
            name=agent_names[i]
        ))

    if(add_broken):
        # Add broken level
        lvl = N_PORTABILITY_LEVELS
        first_result = N_RESULTS * lvl
        last_result = N_RESULTS + first_result
        for i, data in enumerate(agents_data):
            graph_data = loadDimensionData(data, first_result, last_result)
            agent_broken_levels_data[i].extend(graph_data)
            level_data_size = len(graph_data)
            broken_level_info = [LEVELS_THESIS_IDS[lvl] for i in range(level_data_size)]

        for i in range(0, n_agents):
            print("`Broken` Trace "+ str(i) +" y: " + printList(agent_broken_levels_data[i]))
            print("`Broken` Trace "+ str(i) +" x: " + printList(broken_level_info))
            fig.add_trace(go.Histogram(
                y=agent_broken_levels_data[i],
                x=broken_level_info,
                name=agent_names[i]
            ))

    fig.update_layout(
        title=plot_info.title,
        yaxis_title=dimension_name,
        showlegend=True,
        yaxis_range=plot_info.yaxis_range,
        boxmode='group'
    )

    fig.show()
    pio.write_image(fig, GRAPHS_PATH+plot_info.img_title+".pdf", format='pdf')

def loadScores(all_data, row_start, row_end):
    # From: Record breaker stats
    # score lastScoreChange lastPositiveScoreChange
    # We are interested in score: 0
    scores = all_data[:,0][row_start:row_end]
    return scores

def loadCuriosity(all_data, row_start, row_end):
    # From: Curious stats
    # nUniqueSpriteInteractions nCuriosityInteractions nTotalCollisions nTotalHits lastNewCollisionTick lastNewHitTick lastCuriosityTick
    # We are interested in nCuriosityInteractions: 1
    curiosity = all_data[:,1][row_start:row_end]
    return curiosity

def loadCollisions(all_data, row_start, row_end):
    # From: Curious stats
    # nUniqueSpriteInteractions nCuriosityInteractions nTotalCollisions nTotalHits lastNewCollisionTick lastNewHitTick lastCuriosityTick
    # We are interested in nTotalCollisions: 2
    collisions = all_data[:,2][row_start:row_end]
    return collisions

def loadWins(all_data, column_start, column_end):
    # From: Winner
    # Victory? Victory? Victory? ...
    all_results = all_data[column_start:column_end]
    wins = [i for i in all_results if i != 0]
    # We populate one data so at least the graph is displayed. We will remove it with post-processing.
    if len(wins) == 0:
        return [None]
    return wins

def loadEoG(all_data, column_start, column_end):
    # From: Game
    # EoG EoG EoG ...
    eog_ticks = all_data[column_start:column_end]
    return eog_ticks

def loadExploration(all_data, row_start, row_end):
    # From: Explorer
    # nExplored percentageExplored lastNewExplorationTick
    # We are interested in percentageExplored: 1
    exploration = all_data[:,1][row_start:row_end]
    exploration_rate = [i*100 for i in exploration]
    return exploration_rate

def getTitle(game, dimension):
    return game+" Resulting "+ dimension + " per level"

def getTitleBroken(game, dimension):
    return game+" Resulting "+ dimension + " comparison with `Broken` level"

def generatePlots(game, dimension, data, loadDataMethod, agents_info, image_title, yaxis_range=None):
    plot_info = PlotInfo(getTitle(game, dimension), image_title, yaxis_range)
    plot_info_broken = PlotInfo(getTitleBroken(game, dimension), image_title+"_broken", yaxis_range)
    PlotsPortabilityAll(data, loadDataMethod, dimension, agents_info, plot_info)
    PlotsPortabilityAll(data, loadDataMethod, dimension, agents_info, plot_info_broken, True)

def generateHistograms(game, dimension, data, loadDataMethod, agents_info, image_title, yaxis_range=None):
    plot_info = PlotInfo(getTitle(game, dimension), image_title, yaxis_range)
    plot_info_broken = PlotInfo(getTitleBroken(game, dimension), image_title+"_broken", yaxis_range)
    HistogramsPortabilityAll(data, loadDataMethod, dimension, agents_info, plot_info)
    HistogramsPortabilityAll(data, loadDataMethod, dimension, agents_info, plot_info_broken, True)

# Butterflies
game = B3

# Score: E1, E2
if(True):
    dimension = SCORE
    b3_score_e1 = getFileResultsData(B3_E1_RECORDBREAKER)
    b3_score_e2 = getFileResultsData(B3_E2_RECORDBREAKER)
    data = [b3_score_e1, b3_score_e2]
    agents = ["E1", "E2"]
    image_title = game + "_" + dimension + "_E1E2"
    generatePlots(game, dimension, data, loadScores, agents, image_title)


# plot_info = PlotInfo(getTitle(game, SCORE), image_title)
# plot_info_broken = PlotInfo(getTitleBroken(game, SCORE), image_title+"_broken")
# PlotsPortabilityAll(b3_score, loadScores, SCORE, b3_score_agents, plot_info)
# PlotsPortabilityAll(b3_score, loadScores, SCORE, b3_score_agents, plot_info_broken, True)

# Curiosity: E3, E6
if(True):
    dimension = CURIOSITY
    b3_curious_e3 = getFileResultsData(B3_E3_CURIOUS)
    b3_curious_e6 = getFileResultsData(B3_E6_CURIOUS)
    data = [b3_curious_e3, b3_curious_e6]
    agents = ["E3", "E6"]
    image_title = game + "_" + dimension + "_E3E6"
    generatePlots(game, dimension, data, loadCuriosity, agents, image_title)

# Collisions: E3
if(True):
    dimension = COLLISIONS
    b3_curious_e3 = getFileResultsData(B3_E3_CURIOUS)
    data = [b3_curious_e3]
    agents = ["E3"]
    image_title = game + "_" + dimension + "_E3"
    generatePlots(game, dimension, data, loadCollisions, agents, image_title)


# Win rate: E4
if(True):
    dimension = WIN_RATE
    b3_winner_e4 = getFileResultsDataInOneRow(B3_E4_WINNER)
    data = [b3_winner_e4]
    agents = ["E4"]
    image_title = game + "_" + dimension + "_E4"
    generateHistograms(game, dimension, data, loadWins, agents, image_title, [0,100])

# Win rate: E1, E2, E3, E4, E5, E6

# EoG: E4
if(True):
    dimension = EOG
    b3_game_e4 = getFileResultsDataInOneRow(B3_E4_GAME)
    data = [b3_game_e4]
    agents = ["E4"]
    image_title = game + "_" + dimension + "_E4"
    generatePlots(game, dimension, data, loadEoG, agents, image_title, [0,2000])

# Exploration: E5, E6
if(True):
    dimension = EXPLORATION
    b3_explorer_e5 = getFileResultsData(B3_E5_EXPLORER)
    b3_explorer_e6 = getFileResultsData(B3_E6_EXPLORER)
    data = [b3_explorer_e5, b3_explorer_e6]
    agents = ["E5", "E6"]
    image_title = game + "_" + dimension + "_E5E6"
    generatePlots(game, dimension, data, loadExploration, agents, image_title, [0,100])
