# BUTTERFLIES: screencapture -v -R 0,23,783,330 testButterflies.webm
# ZELDA: screencapture -v -R 0,23,792,320 testZelda.webm
# DIGDUG: screencapture -v -R 0,23,810,472 testDigdug.webm

# <game>_<experimentId>_<cellX>_<cellY>.json
# <game>_<experimentId>_<cellX>_<cellY>.webm

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





