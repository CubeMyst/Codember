#!/bin/bash decypher

if [ $# -ne 1 ]; then
    echo "Uso: $0 <ruta del archivo txt>"
    exit 1
fi

input_file="$1"
numeric_value=0
output=""

while IFS= read -r -n 1 symbol; do
    if [ "$symbol" == "#" ]; then
        numeric_value=$((numeric_value + 1))
    elif [ "$symbol" == "@" ]; then
        numeric_value=$((numeric_value - 1))
    elif [ "$symbol" == "*" ]; then
        numeric_value=$((numeric_value * numeric_value))
    elif [ "$symbol" == "&" ]; then
        output="${output}${numeric_value}"
    fi
done < "$input_file"

echo "$output"