#!/usr/bin/env bash

filename="$1"

all_lines=`cat $filename`

for item in $all_lines;
do
    git clone --depth 1 "$item" temp-linecount-repo &&
    printf "('temp-linecount-repo' will be deleted automatically)\n\n\n" &&
    cloc temp-linecount-repo &&
    rm -rf temp-linecount-repo

    echo $item
done
