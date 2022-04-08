#! /bin/sh
# moveTag.sh moves the line of tag to the end of a file.

for file in "$@"; do
    echo "\n" >> $file;
    grep '#[a-zA-Z]' "$file" | head -n 1 >> "$file";
    gsed -i '/#[a-zA-Z]/{1,3d}' "$file"
done

# sed '/#[a-zA-Z]/d' test.md


