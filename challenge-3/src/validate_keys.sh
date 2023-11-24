#!/bin/bash

# Check if the filename is provided as an argument
if [ "$#" -eq 0 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

filename="$1"

# Function to check if a key is valid
is_valid_key() {
    local policy=$1
    local key=$2

    IFS=' ' read -r -a policy_array <<<"$policy"
    IFS='-' read -r min max <<<"${policy_array[0]}"
    char="${policy_array[1]::1}"

    count=$(grep -o "$char" <<<"$key" | wc -l)

    if ((count >= min && count <= max)); then
        return 0 # Valid key
    else
        return 1 # Invalid key
    fi
}

# Read the file line by line
invalid_count=0
while IFS= read -r line; do
    IFS=':' read -r policy key <<<"$line"

    if ! is_valid_key "$policy" "$key"; then
        ((invalid_count++))

        # Check if it's the 42nd invalid key
        if ((invalid_count == 42)); then
            echo "The 42nd invalid key is: $key"
            exit
        fi
    fi
done <"$filename"

echo "Number of valid keys: $(($(wc -l <"$filename") - invalid_count))"
