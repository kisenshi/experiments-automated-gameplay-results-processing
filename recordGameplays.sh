# Run and record automated gameplays for Butterflies, Zelda, Digdug and Sheriff
# based on the json config files provided. Makes use of the project
# "automatedGameplay". The implementation of this standalone project can be found at 
# https://github.com/kisenshi/gvgai-heuristic-extension/tree/automated-gameplay-standalone
# The work is related to the one presented at "MAP-Elites to Generate a Team of 
# Agents that Elicits Diverse Automated Gameplay" so refer to it for more
# details about the data, agents and motivation.
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

#!/usr/bin/env bash

if [ "$#" -ne 2 ]; then
    echo "Illegal number of parameters. 1st: folder; 2nd: game"
    exit -1
fi

echo "automatedGameplay"
cd automatedGameplay

case $2 in
	BUTTERFLIES)
		echo "Running automated gameplays of butterflies"
        captureSize="0,23,783,330"
		;;
    ZELDA)
		echo echo "Running automated gameplays of zelda"
        captureSize="0,23,792,320"
		;;
	DIGDUG)
		echo "Running automated gameplays of digdug"
        captureSize="0,23,810,472"
		;;
    SHERIFF)
		echo "Running automated gameplays of sheriff"
        captureSize="0,23,799,373"
		break
		;;
    *)
        echo "Not expected to print this ever"
        ;;
  esac

for file in configFiles/$1/*
    do
        echo "Processing $file"
        fileName="$(basename $file .json)"

        # Start video recording in a new tab
        echo "ttab 'sh record-screen.sh $captureSize $fileName'"
        ttab "sh record-screen.sh $captureSize $fileName"

        # Run automated gameplay
        echo "java -jar RunAutomatedGameplay-exit.jar $file"
        java -jar RunAutomatedGameplay-exit.jar $file

        # Kill screen capture process
        echo "Kill screencapture process: pkill -f record-screen.sh"
        pkill -f record-screen.sh

        echo "mv $file configFiles/processed/"
        mv $file configFiles/processed/

        echo ""
    done





