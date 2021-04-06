# Generates all the resulting MAPElites in png format

echo "python mapElitesData.py B2"
python mapElitesData.py B2

echo "python mapElitesData.py B3"
python mapElitesData.py B3

for experiment in a b c d f g h
    do
        echo "python mapElitesData.py Z5/config30Z1$experiment 125"
        python mapElitesData.py Z5/config30Z1$experiment 125
    done

for experiment in a b c d e f g h i j
    do
        echo "python mapElitesData.py D5/config30D0$experiment 100"
        python mapElitesData.py D5/config30D0$experiment 100
    done