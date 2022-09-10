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
Z5 = "Z5"
D5 = "D5"
S4 = "S4"

# DIMENSIONS
SCORE           = "Score"
CURIOSITY       = "Curiosity"
COLLISIONS      = "Collisions"
WIN_RATE        = "Victories"
EOG             = "EoG"
KILLS           = "Kills"
EXPLORATION     = "Exploration"
ITEMS           = "Items"
HITS            = "Hits"
INTERACTIONS    = "Interactions"

# BUTTERFLIES

LEVELS_THESIS_IDS_BUTTERFLIES = [
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
B3_E1_WINNER        = B3_RESULTS+"E1/B3_E1_winner.txt"
B3_E2_WINNER        = B3_RESULTS+"E2/B3_E2_winner.txt"
B3_E3_WINNER        = B3_RESULTS+"E3/B3_E3_winner.txt"
B3_E5_WINNER        = B3_RESULTS+"E5/B3_E5_winner.txt"
B3_E6_WINNER        = B3_RESULTS+"E6/B3_E6_winner.txt"
B3_E1_EXPLORER      = B3_RESULTS+"E1/B3_E1_explorer.txt"
B3_E2_EXPLORER      = B3_RESULTS+"E2/B3_E2_explorer.txt"
B3_E3_EXPLORER      = B3_RESULTS+"E3/B3_E3_explorer.txt"
B3_E4_EXPLORER      = B3_RESULTS+"E4/B3_E4_explorer.txt"

# ZELDA

LEVELS_THESIS_IDS_ZELDA = [
    "7.2b",
    "7.28a",
    "7.28b",
    "7.28c",
    "7.28d",
    "`Broken`"
]

Z5_RESULTS = "generalisation/results_Z5/"

Z5_E1_RECORDBREAKER = Z5_RESULTS+"E1/Z5_E1_record_breaker.txt"
Z5_E2_WINNER        = Z5_RESULTS+"E2/Z5_E2_winner.txt"
Z5_E2_GAME          = Z5_RESULTS+"E2/Z5_E2_game.txt"
Z5_E3_EXPLORER      = Z5_RESULTS+"E3/Z5_E3_explorer.txt"
Z5_E5_EXPLORER      = Z5_RESULTS+"E5/Z5_E5_explorer.txt"
Z5_E6_EXPLORER      = Z5_RESULTS+"E6/Z5_E6_explorer.txt"
Z5_E4_KILLER        = Z5_RESULTS+"E4/Z5_E4_killer.txt"
Z5_E5_KILLER        = Z5_RESULTS+"E5/Z5_E5_killer.txt"
Z5_E6_KILLER        = Z5_RESULTS+"E6/Z5_E6_killer.txt"
Z5_E1_WINNER        = Z5_RESULTS+"E1/Z5_E1_winner.txt"
Z5_E3_WINNER        = Z5_RESULTS+"E3/Z5_E3_winner.txt"
Z5_E4_WINNER        = Z5_RESULTS+"E4/Z5_E4_winner.txt"
Z5_E5_WINNER        = Z5_RESULTS+"E5/Z5_E5_winner.txt"
Z5_E6_WINNER        = Z5_RESULTS+"E6/Z5_E6_winner.txt"
Z5_E1_GAME          = Z5_RESULTS+"E1/Z5_E1_game.txt"
Z5_E3_GAME          = Z5_RESULTS+"E3/Z5_E3_game.txt"
Z5_E4_GAME          = Z5_RESULTS+"E4/Z5_E4_game.txt"
Z5_E5_GAME          = Z5_RESULTS+"E5/Z5_E5_game.txt"
Z5_E6_GAME          = Z5_RESULTS+"E6/Z5_E6_game.txt"

# DIGDUG

LEVELS_THESIS_IDS_DIGDUG = [
    "7.2c",
    "7.36a",
    "7.36b",
    "7.36c",
    "7.36d",
    "`Broken`"
]

D5_RESULTS = "generalisation/results_D5/"

D5_E1_KILLER        = D5_RESULTS+"E1/D5_E1_killer.txt"
D5_E1_COLLECTOR     = D5_RESULTS+"E1/D5_E1_collector.txt"
D5_E2_KILLER        = D5_RESULTS+"E2/D5_E2_killer.txt"
D5_E2_COLLECTOR     = D5_RESULTS+"E2/D5_E2_collector.txt"
D5_E3_KILLER        = D5_RESULTS+"E3/D5_E3_killer.txt"
D5_E3_COLLECTOR     = D5_RESULTS+"E3/D5_E3_collector.txt"
D5_E4_EXPLORER      = D5_RESULTS+"E4/D5_E4_explorer.txt"
D5_E4_CURIOUS       = D5_RESULTS+"E4/D5_E4_curious.txt"
D5_E5_EXPLORER      = D5_RESULTS+"E5/D5_E5_explorer.txt"
D5_E6_EXPLORER      = D5_RESULTS+"E6/D5_E6_explorer.txt"
D5_E6_RECORDBREAKER = D5_RESULTS+"E6/D5_E6_record_breaker.txt"

# SHERIFF

LEVELS_THESIS_IDS_SHERIFF = [
    "7.2d",
    "7.43a",
    "7.43b",
    "7.43c",
    "7.43d",
    "`Broken`"
]

S4_RESULTS = "generalisation/results_S4/"

S4_E1_WINNER        = S4_RESULTS+"E1/S4_E1_winner.txt"
S4_E1_KILLER        = S4_RESULTS+"E1/S4_E1_killer.txt"
S4_E1_GAME          = S4_RESULTS+"E1/S4_E1_game.txt"
S4_E2_EXPLORER      = S4_RESULTS+"E2/S4_E2_explorer.txt"
S4_E2_KILLER        = S4_RESULTS+"E2/S4_E2_killer.txt"
S4_E3_EXPLORER      = S4_RESULTS+"E3/S4_E3_explorer.txt"
S4_E3_KILLER        = S4_RESULTS+"E3/S4_E3_killer.txt"
S4_E4_WINNER        = S4_RESULTS+"E4/S4_E4_winner.txt"
S4_E4_GAME          = S4_RESULTS+"E4/S4_E4_game.txt"
S4_E5_CURIOUS       = S4_RESULTS+"E5/S4_E5_curious.txt"
S4_E5_KILLER        = S4_RESULTS+"E5/S4_E5_killer.txt"
S4_E6_CURIOUS       = S4_RESULTS+"E6/S4_E6_curious.txt"

# PLOTS

LEVELS_THESIS_IDS = LEVELS_THESIS_IDS_SHERIFF

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

def getFileResultsData(file_name, n_cols=3):
	print("Reading "+file_name)

	files = glob.glob(file_name)
	if len(files) == 0:
		print("Missing file: ", file_name)
		return None

	return pylab.loadtxt(files[0], comments='*', delimiter=' ', usecols=range(n_cols))

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
        xaxis_title="Level",
        showlegend=True,
        yaxis_range=plot_info.yaxis_range,
        boxmode='group'
    )

    fig.show()
    pio.full_figure_for_development(fig, warn=False) # Remove weird error message in image.
    pio.write_image(fig, GRAPHS_PATH+plot_info.img_title+".pdf", format='pdf')

# HistogramsPortabilityAll generates an histogram instead of a whisker plot.
def HistogramsPortabilityAll(agents_data, loadDimensionData, dimension_name, agent_names, plot_info, add_broken=False):
    fig = go.Figure()

    # For portability, we do not include the result of the broken level.
    # Populate level information for each agent.
    n_agents = len(agents_data)
    levels_info = [[] for i in range(n_agents)]
    broken_levels_info = [[] for i in range(n_agents)]
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
            levels_info[i].extend(level_info)

    # Create plots for each agent so they are grouped.
    for i in range(0, n_agents):
        print("Trace "+ str(i) +" y" + printList(agent_levels_data[i]))
        print("Trace "+ str(i) +" x" + printList(levels_info[i]))
        fig.add_trace(go.Histogram(
            y=agent_levels_data[i],
            x=levels_info[i],
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
            broken_levels_info[i] = [LEVELS_THESIS_IDS[lvl] for i in range(level_data_size)]

        for i in range(0, n_agents):
            print("`Broken` Trace "+ str(i) +" y: " + printList(agent_broken_levels_data[i]))
            print("`Broken` Trace "+ str(i) +" x: " + printList(broken_levels_info[i]))
            fig.add_trace(go.Histogram(
                y=agent_broken_levels_data[i],
                x=broken_levels_info[i],
                name=agent_names[i]
            ))

    fig.update_layout(
        title=plot_info.title,
        yaxis_title=dimension_name,
        xaxis_title="Level",
        showlegend=True,
        yaxis_range=plot_info.yaxis_range,
        boxmode='group'
    )

    fig.show()
    pio.full_figure_for_development(fig, warn=False) # Remove weird error message in image.
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

def loadHits(all_data, row_start, row_end):
    # From: Curious stats
    # nUniqueSpriteInteractions nCuriosityInteractions nTotalCollisions nTotalHits lastNewCollisionTick lastNewHitTick lastCuriosityTick
    # We are interested in nTotalHits: 3
    hits = all_data[:,3][row_start:row_end]
    return hits

def loadInteractions(all_data, row_start, row_end):
    # From: Curious stats
    # nUniqueSpriteInteractions nCuriosityInteractions nTotalCollisions nTotalHits lastNewCollisionTick lastNewHitTick lastCuriosityTick
    # We are interested in: nInteractions = nTotalCollisions + nTotalHits
    collisions = loadCollisions(all_data, row_start, row_end)
    hits = loadHits(all_data, row_start, row_end)
    interactions = [collisions[i]+hits[i] for i in range(len(collisions))]
    return interactions

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

def loadKills(all_data, row_start, row_end):
    # From: Killer
    # nTotalKills lastKillTick
    # We are interested in nTotalKills : 0
    kills = all_data[:,0][row_start:row_end]
    return kills

def loadItems(all_data, row_start, row_end):
    # From: Collector
    # nTotalItemsCollected lastCollectionTick
    # We are interested in nTotalItemsCollected: 0
    items = all_data[:,0][row_start:row_end]
    return items

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

#################################################################################################
# Butterflies
#################################################################################################
game = B3

# Score: E1, E2
if(False):
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
if(False):
    dimension = CURIOSITY
    b3_curious_e3 = getFileResultsData(B3_E3_CURIOUS)
    b3_curious_e6 = getFileResultsData(B3_E6_CURIOUS)
    data = [b3_curious_e3, b3_curious_e6]
    agents = ["E3", "E6"]
    image_title = game + "_" + dimension + "_E3E6"
    generatePlots(game, dimension, data, loadCuriosity, agents, image_title)

# Collisions: E3
if(False):
    dimension = COLLISIONS
    b3_curious_e3 = getFileResultsData(B3_E3_CURIOUS)
    data = [b3_curious_e3]
    agents = ["E3"]
    image_title = game + "_" + dimension + "_E3"
    generatePlots(game, dimension, data, loadCollisions, agents, image_title)


# Win rate: E4
if(False):
    dimension = WIN_RATE
    b3_winner_e4 = getFileResultsDataInOneRow(B3_E4_WINNER)
    data = [b3_winner_e4]
    agents = ["E4"]
    image_title = game + "_" + dimension + "_E4"
    generateHistograms(game, dimension, data, loadWins, agents, image_title, [0,100])

# Win rate: E1, E2, E3, E4, E5, E6
if(False):
    dimension = WIN_RATE
    b3_winner_e1 = getFileResultsDataInOneRow(B3_E1_WINNER)
    b3_winner_e2 = getFileResultsDataInOneRow(B3_E2_WINNER)
    b3_winner_e3 = getFileResultsDataInOneRow(B3_E3_WINNER)
    b3_winner_e4 = getFileResultsDataInOneRow(B3_E4_WINNER)
    b3_winner_e5 = getFileResultsDataInOneRow(B3_E5_WINNER)
    b3_winner_e6 = getFileResultsDataInOneRow(B3_E6_WINNER)
    data = [b3_winner_e1, b3_winner_e2, b3_winner_e3, b3_winner_e4, b3_winner_e5, b3_winner_e6]
    agents = ["E1","E2","E3","E4","E5","E6"]
    image_title = game + "_" + dimension + "_E1E2E3E4E5E6"
    generateHistograms(game, dimension, data, loadWins, agents, image_title, [0,100])

# EoG: E4
if(False):
    dimension = EOG
    b3_game_e4 = getFileResultsDataInOneRow(B3_E4_GAME)
    data = [b3_game_e4]
    agents = ["E4"]
    image_title = game + "_" + dimension + "_E4"
    generatePlots(game, dimension, data, loadEoG, agents, image_title, [0,2000])

# Exploration: E5, E6
if(False):
    dimension = EXPLORATION
    b3_explorer_e5 = getFileResultsData(B3_E5_EXPLORER)
    b3_explorer_e6 = getFileResultsData(B3_E6_EXPLORER)
    data = [b3_explorer_e5, b3_explorer_e6]
    agents = ["E5", "E6"]
    image_title = game + "_" + dimension + "_E5E6"
    generatePlots(game, dimension, data, loadExploration, agents, image_title, [0,100])

# Exploration: E1, E2, E3, E4, E5, E6
if(False):
    dimension = EXPLORATION
    b3_explorer_e1 = getFileResultsData(B3_E1_EXPLORER)
    b3_explorer_e2 = getFileResultsData(B3_E2_EXPLORER)
    b3_explorer_e3 = getFileResultsData(B3_E3_EXPLORER)
    b3_explorer_e4 = getFileResultsData(B3_E4_EXPLORER)
    b3_explorer_e5 = getFileResultsData(B3_E5_EXPLORER)
    b3_explorer_e6 = getFileResultsData(B3_E6_EXPLORER)
    data = [b3_explorer_e1, b3_explorer_e2, b3_explorer_e3, b3_explorer_e4, b3_explorer_e5, b3_explorer_e6]
    agents = ["E1", "E2", "E3", "E4", "E5", "E6"]
    image_title = game + "_" + dimension + "_E1E2E3E4E5E6"
    generatePlots(game, dimension, data, loadExploration, agents, image_title, [0,100])

#################################################################################################
# Zelda
#################################################################################################
game = Z5

# Score: E1
if(False):
    dimension = SCORE
    z5_score_e1 = getFileResultsData(Z5_E1_RECORDBREAKER)
    data = [z5_score_e1]
    agents = ["E1"]
    image_title = game + "_" + dimension + "_E1"
    generatePlots(game, dimension, data, loadScores, agents, image_title)

# Victories: E2
if(False):
    dimension = WIN_RATE
    z5_winner_e2 = getFileResultsDataInOneRow(Z5_E2_WINNER)
    data = [z5_winner_e2]
    agents = ["E2"]
    image_title = game + "_" + dimension + "_E2"
    generateHistograms(game, dimension, data, loadWins, agents, image_title, [0,100])

# EoG: E2
if(False):
    dimension = EOG
    z5_game_e2 = getFileResultsDataInOneRow(Z5_E2_GAME)
    data = [z5_game_e2]
    agents = ["E2"]
    image_title = game + "_" + dimension + "_E2"
    generatePlots(game, dimension, data, loadEoG, agents, image_title, [0,2000])

# Exploration: E3, E5, E6
if(False):
    dimension = EXPLORATION
    z5_explorer_e3 = getFileResultsData(Z5_E3_EXPLORER)
    z5_explorer_e5 = getFileResultsData(Z5_E5_EXPLORER)
    z5_explorer_e6 = getFileResultsData(Z5_E6_EXPLORER)
    data = [z5_explorer_e3, z5_explorer_e5, z5_explorer_e6]
    agents = ["E3", "E5", "E6"]
    image_title = game + "_" + dimension + "_E3E5E6"
    generatePlots(game, dimension, data, loadExploration, agents, image_title, [0,100])

# Kills: E4, E5, E6
if(False):
    dimension = KILLS
    z5_killer_e4 = getFileResultsData(Z5_E4_KILLER, 2)
    z5_killer_e5 = getFileResultsData(Z5_E5_KILLER, 2)
    z5_killer_e6 = getFileResultsData(Z5_E6_KILLER, 2)
    data = [z5_killer_e4, z5_killer_e5, z5_killer_e6]
    agents = ["E4", "E5", "E6"]
    image_title = game + "_" + dimension + "_E4E5E6"
    generatePlots(game, dimension, data, loadKills, agents, image_title)

# All agents comparison: Victories and EoG.
# Victories
if(False):
    dimension = WIN_RATE
    z5_winner_e1 = getFileResultsDataInOneRow(Z5_E1_WINNER)
    z5_winner_e2 = getFileResultsDataInOneRow(Z5_E2_WINNER)
    z5_winner_e3 = getFileResultsDataInOneRow(Z5_E3_WINNER)
    z5_winner_e4 = getFileResultsDataInOneRow(Z5_E4_WINNER)
    z5_winner_e5 = getFileResultsDataInOneRow(Z5_E5_WINNER)
    z5_winner_e6 = getFileResultsDataInOneRow(Z5_E6_WINNER)
    data = [z5_winner_e1, z5_winner_e2, z5_winner_e3, z5_winner_e4, z5_winner_e5, z5_winner_e6]
    agents = ["E1", "E2", "E3", "E4", "E5", "E6"]
    image_title = game + "_" + dimension + "_E1E2E3E4E5E6"
    generateHistograms(game, dimension, data, loadWins, agents, image_title, [0,100])

# EoG
if(False):
    dimension = EOG
    z5_game_e1 = getFileResultsDataInOneRow(Z5_E1_GAME)
    z5_game_e2 = getFileResultsDataInOneRow(Z5_E2_GAME)
    z5_game_e3 = getFileResultsDataInOneRow(Z5_E3_GAME)
    z5_game_e4 = getFileResultsDataInOneRow(Z5_E4_GAME)
    z5_game_e5 = getFileResultsDataInOneRow(Z5_E5_GAME)
    z5_game_e6 = getFileResultsDataInOneRow(Z5_E6_GAME)
    data = [z5_game_e1, z5_game_e2, z5_game_e3, z5_game_e4, z5_game_e5, z5_game_e6]
    agents = ["E1", "E2", "E3", "E4", "E5", "E6"]
    image_title = game + "_" + dimension + "_E1E2E3E4E5E6"
    generatePlots(game, dimension, data, loadEoG, agents, image_title, [0,2000])

#################################################################################################
# Digdug
#################################################################################################
game = D5

# Kills: E1, E2, E3
if(False):
    dimension = KILLS
    d5_killer_e1 = getFileResultsData(D5_E1_KILLER, 2)
    d5_killer_e2 = getFileResultsData(D5_E2_KILLER, 2)
    d5_killer_e3 = getFileResultsData(D5_E3_KILLER, 2)
    data = [d5_killer_e1, d5_killer_e2, d5_killer_e3]
    agents = ["E1", "E2", "E3"]
    image_title = game + "_" + dimension + "_E1E2E3"
    generatePlots(game, dimension, data, loadKills, agents, image_title)

# Items: E1, E2, E3
if(False):
    dimension = ITEMS
    d5_collector_e1 = getFileResultsData(D5_E1_COLLECTOR, 2)
    d5_collector_e2 = getFileResultsData(D5_E2_COLLECTOR, 2)
    d5_collector_e3 = getFileResultsData(D5_E3_COLLECTOR, 2)
    data = [d5_collector_e1, d5_collector_e2, d5_collector_e3]
    agents = ["E1", "E2", "E3"]
    image_title = game + "_" + dimension + "_E1E2E3"
    generatePlots(game, dimension, data, loadItems, agents, image_title)

# Exploration: E4, E5, E6
if(False):
    dimension = EXPLORATION
    d5_explorer_e4 = getFileResultsData(D5_E4_EXPLORER)
    d5_explorer_e5 = getFileResultsData(D5_E5_EXPLORER)
    d5_explorer_e6 = getFileResultsData(D5_E6_EXPLORER)
    data = [d5_explorer_e4, d5_explorer_e5, d5_explorer_e6]
    agents = ["E4", "E5", "E6"]
    image_title = game + "_" + dimension + "_E4E5E6"
    generatePlots(game, dimension, data, loadExploration, agents, image_title, [0,100])

# Curiosity: E4
if(False):
    dimension = CURIOSITY
    d5_curious_e4 = getFileResultsData(D5_E4_CURIOUS, 7)
    data = [d5_curious_e4]
    agents = ["E4"]
    image_title = game + "_" + dimension + "_E4"
    generatePlots(game, dimension, data, loadCuriosity, agents, image_title)

# Hits: E4
if(False):
    dimension = HITS
    d5_curious_e4 = getFileResultsData(D5_E4_CURIOUS, 7)
    data = [d5_curious_e4]
    agents = ["E4"]
    image_title = game + "_" + dimension + "_E4"
    generatePlots(game, dimension, data, loadHits, agents, image_title)

# Score: E6
if(False):
    dimension = SCORE
    d5_score_e6 = getFileResultsData(D5_E6_RECORDBREAKER)
    data = [d5_score_e6]
    agents = ["E6"]
    image_title = game + "_" + dimension + "_E6"
    generatePlots(game, dimension, data, loadScores, agents, image_title)

#################################################################################################
# Sheriff
#################################################################################################
game = S4

# Victories: E1, E4
if(True):
    dimension = WIN_RATE
    s4_winner_e1 = getFileResultsDataInOneRow(S4_E1_WINNER)
    s4_winner_e4 = getFileResultsDataInOneRow(S4_E4_WINNER)
    data = [s4_winner_e1, s4_winner_e4]
    agents = ["E1", "E4"]
    image_title = game + "_" + dimension + "_E1E4"
    generateHistograms(game, dimension, data, loadWins, agents, image_title, [0,100])

# Kills: E1, E2, E3, E5
if(True):
    dimension = KILLS
    s4_killer_e1 = getFileResultsData(S4_E1_KILLER, 2)
    s4_killer_e2 = getFileResultsData(S4_E2_KILLER, 2)
    s4_killer_e3 = getFileResultsData(S4_E3_KILLER, 2)
    s4_killer_e5 = getFileResultsData(S4_E5_KILLER, 2)
    data = [s4_killer_e1, s4_killer_e2, s4_killer_e3, s4_killer_e5]
    agents = ["E1", "E2", "E3", "E5"]
    image_title = game + "_" + dimension + "_E1E2E3E5"
    generatePlots(game, dimension, data, loadKills, agents, image_title)

# EoG: E1, E4
if(True):
    dimension = EOG
    s4_game_e1 = getFileResultsDataInOneRow(S4_E1_GAME)
    s4_game_e4 = getFileResultsDataInOneRow(S4_E4_GAME)
    data = [s4_game_e1, s4_game_e4]
    agents = ["E1", "E4"]
    image_title = game + "_" + dimension + "_E1E4"
    generatePlots(game, dimension, data, loadEoG, agents, image_title, [0,1000])

# Exploration: E2, E3
if(True):
    dimension = EXPLORATION
    s4_explorer_e2 = getFileResultsData(S4_E2_EXPLORER)
    s4_explorer_e3 = getFileResultsData(S4_E3_EXPLORER)
    data = [s4_explorer_e2, s4_explorer_e3]
    agents = ["E2", "E3"]
    image_title = game + "_" + dimension + "_E2E3"
    generatePlots(game, dimension, data, loadExploration, agents, image_title, [0,100])

# Interactions: E5, E6
if(True):
    dimension = INTERACTIONS
    s4_curious_e5 = getFileResultsData(S4_E5_CURIOUS, 7)
    s4_curious_e6 = getFileResultsData(S4_E6_CURIOUS, 7)
    data = [s4_curious_e5, s4_curious_e6]
    agents = ["E5", "E6"]
    image_title = game + "_" + dimension + "_E5E6"
    generatePlots(game, dimension, data, loadInteractions, agents, image_title)

# Hits: E5
if(True):
    dimension = HITS
    s4_curious_e5 = getFileResultsData(S4_E5_CURIOUS, 7)
    data = [s4_curious_e5]
    agents = ["E5"]
    image_title = game + "_" + dimension + "_E5"
    generatePlots(game, dimension, data, loadHits, agents, image_title)

# Curiosity: E6
if(True):
    dimension = CURIOSITY
    s4_curious_e6 = getFileResultsData(S4_E6_CURIOUS, 7)
    data = [s4_curious_e6]
    agents = ["E6"]
    image_title = game + "_" + dimension + "_E6"
    generatePlots(game, dimension, data, loadCuriosity, agents, image_title)