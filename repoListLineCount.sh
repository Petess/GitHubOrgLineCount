#!/usr/bin/env bash

filename="$1"

all_lines=`cat $filename`

for item in $all_lines;
do
    printf "Repository : $item\n" 
    projectName=${item:0:${#item}-4}
    projectName2=${projectName##*/}
    
    git clone --depth 1 "$item" temp-linecount-repo &&
    printf "('temp-linecount-repo' will be deleted automatically)\n\n\n" &&
    cloc --sql 1 --sql-project $projectName2 --sql-append temp-linecount-repo | sqlite3 code3.db
    rm -rf temp-linecount-repo

    echo $item
done
