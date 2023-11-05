#!/bin/bash

# Author: CubeMyst

if [ $# -ne 1 ]; then
    echo "Usó: $0 archivo.txt"
    exit 1
fi

file="$1"

if [ ! -f "$file" ]; then
    echo "El archivo $file no existe!!!"
    exit 1
fi

result=""
count=0
word_key=""

while IFS= read -r word; do
    if [ "$word" == "$word_key" ]; then
        count=$((count + 1))
    else
        if [ -n "$result" ]; then
            result="${result}${count}${word_key}"
        else
            result="${count}${word_key}"
        fi
        word_key="$word"
        count=1
    fi
done < <(cat "$file" | tr -s ' ' '\n' | sort)

if [ -n "$result" ]; then
    result="${result}${count}${word_key}"
fi

echo "$result"