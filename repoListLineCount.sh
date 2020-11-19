#!/usr/bin/env bash

filename="$1"
projectTotalsDir="$2" 

all_lines=`cat $filename`

if (( $# != 2 )); then
    >&2 echo "Required parameters - filename resultsDirectory"
fi

mkdir temp-repo
mkdir $projectTotalsDirOA

for item in $all_lines;
do
    printf "Repository : $item\n" 
    projectName=${item:0:${#item}-4}
    projectName2=${projectName##*/}
    
    git clone --depth 1 "$item" temp-repo/$projectName2 &&
    cloc --out $projectTotalsDir/$projectName2.txt temp-repo/$projectName2 &&
    rm -rf temp-repo/$projectName2 

    echo $item
done

rmdir temp-repo

cloc --csv --sum_reports -out Summary_Results $projectTotalsDir/*.txt


