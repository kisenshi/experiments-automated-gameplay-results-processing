# Merges all Z5 and D5 resulting temp files into one

for experiment in a b c d f g h
    do
        echo "python mergeTempJson.py Z5/config30Z1$experiment 125"
        python mergeTempJson.py Z5/config30Z1$experiment 125
    done

for experiment in a b c d e f g h i j
    do
        echo "python mergeTempJson.py D5/config30D0$experiment 100"
        python mergeTempJson.py D5/config30D0$experiment 100
    done