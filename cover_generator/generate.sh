#!/bin/bash

if [ $# != 2 ]; then
    echo "ERROR: Invalid number of command line arguments!"
    echo "Usage: generator.sh <volume> <year>"
    exit 1
fi

VOLUME=$1
YEAR=$2

topics[0]="Elementary Mathematics" 
topics[1]="Science Popularizer Mathematics" 
topics[2]="Mathematics" 
topics[3]="Elementary Physics" 
topics[4]="Science Popularizer Physics" 
topics[5]="Physics" 
topics[6]="Elementary Informatics" 
topics[7]="Science Popularizer Informatics" 
topics[8]="Informatics"

rm -rf _outputs > /dev/null 2>&1
mkdir _outputs

for ((i = 0; i < ${#topics[@]}; i++)); do
    topic=${topics[$i]}
    echo "Generate: ${topic} ..."
    fname=Pi_$(echo ${topic} | sed "s/\ /_/g")_vol_${VOLUME}_${YEAR}.pdf
    rm -rf _temp > /dev/null 2>&1
    cp -r assets _temp
    cd _temp
    sed --in-place "s/TOPIC/${topic}/g" pi_cover.tex
    sed --in-place "s/VOLUME/${VOLUME}/g" pi_cover.tex
    sed --in-place "s/YEAR/${YEAR}/g" pi_cover.tex
    pdflatex pi_cover.tex -o pi_cover.pdf
    mv pi_cover.pdf ../_outputs/${fname}
    cd ..
    rm -rf _temp
done

