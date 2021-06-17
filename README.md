# MAP-Elites to Generate a Team of Agents that Elicits Diverse Automated Gameplay: Scripts and results processing

This repository contains the scripts to process the experiments resulting from the work 
described in [MAP-Elites to Generate a Team of Agents that Elicits Diverse Automated Gameplay](http://kisenshi.github.io/files/paper-map-elites-generation-team-agents-behaviour.pdf).

For more information, refer to the [Github repository with the code to run the experiments](https://github.com/kisenshi/gvgai-agent-behaviour-research) and [OSF repository containing the experiments results and data](https://osf.io/whxm8/).

The scripts implemented allow automatising and processing the resulting JSON files as follows:

- _jsonDataMethods.py_ Process and map resulting MAP-Elites JSON file.

- _mapElitesData.py_ Generate png files with the heatmaps representing the resulting MAP-Elites containing the team of agents. These images have been used in the paper. The whole collection generated can be found in the OSF repository.

- _mergeTempJson.py_ Merge experiment config and temporary JSON file into one, with the format 
of the final results of the experiment. This was needed for the experiments that took a long time and didn't reach the initial number of iterations set (D5 and Z5).

- _generateAutomatedGameplayConfigs.py_ Generate config files to be provided to "automatedGameplay" for each member of the team generated in the MAP-Elites. This allows triggering automated gameplay of the games using the configuration describing each of the agents generated in the experiments.

- _recordGameplays.sh_ Run and record automated gameplays for Butterflies, Zelda and Digdug games. The description of the agent used to run the automated gameplay is provided on a JSON config file. During the execution of the game, we make a call to _record-screen.sh_. This runs screencapture and has been included in the automatedGameplay folder.

- _mergeAll.sh_ Convert all the Z5 and D5 temp files into their final ones at once.

- _generateAll.sh_ Generate all heatmaps at once.

## Credits

We use [Plotly Python](https://plotly.com/python/) to generate the graphs and [ttab](https://www.npmjs.com/package/ttab) to be
able to run screencapture while executing the game.

## License

Copyright (C) 2021 Cristina Guerrero-Romero

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.