#!/usr/bin/env bash

filename="$1"

all_lines=`cat $filename`

for item in $all_lines;
do
    printf "Repository : $item\n" 
    projectName=${item:0:${#item}-4}
    projectName2=${projectName##*/}
    
    git clone --depth 1 "$item" temp-repo/$projectName2 &&
    cloc --out temp-project-totals/$projectName2.txt temp-repo/$projectName2 &&
    rm -rf temp-repo/$projectName2 

    echo $item
done
