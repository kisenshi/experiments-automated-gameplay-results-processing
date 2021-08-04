# https://stackoverflow.com/questions/55257943/ffmpeg-how-to-remove-white-frames
# ffmpeg -i $videoFile -vf blackframe=1,metadata=select:key=lavfi.blackframe.pblack:value=0:function=less -vsync cfr -c:a copy compressed/$videoFile

#!/usr/bin/env bash

if [ "$#" -ne 1 ]; then
    echo "Illegal number of parameters. 1st: folder"
    exit -1
fi

echo "automatedGameplay/videos/$1"
cd automatedGameplay/videos/$1

echo "mkdir compressed"
mkdir compressed

for videoFile in ./*.webm
do
    fileName="$(basename $videoFile .webm)"
    echo "Compresssing and converting $videoFile to $fileName.mp4"

    # Compress video using ffmpeg. The idea for the command comes from the Stackoverflow answer linked above
    # Remove black frames, compress and convert to mp4
    echo "ffmpeg -i $videoFile -vf blackframe=1,metadata=select:key=lavfi.blackframe.pblack:value=0:function=less -vcodec libx264 -vsync cfr -crf 24 compressed/$fileName.mp4"
    ffmpeg -i $videoFile -vf blackframe=1,metadata=select:key=lavfi.blackframe.pblack:value=98:function=less -vcodec libx264 -vsync cfr -crf 24 compressed/$fileName.mp4
    echo ""
done