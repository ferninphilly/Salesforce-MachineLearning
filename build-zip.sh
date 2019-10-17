#!/bin/bash

# to run this, type:
# ./build-zip.sh

# First, create PDF files

for file in class day1 day2 day3 day4 day5; do
    slides=$(python slidelist.py < $file.html)
    decktape remark --slides "$slides" $file.html $file.pdf
done

# Now make the zip file
zip -r $(basename $(pwd)).zip *.pdf src images --exclude 'src/data/*' 'src/.ipynb_checkpoints/*'
