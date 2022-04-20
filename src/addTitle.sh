#! /bin/sh
# addTitle.sh add filename to the start of the note file

for file in "$@"; do 
    sed -Ei '' "1 s~(^.)~# $file\n\1~g" "$file"; # Add relative path to head if it's blank
    sed -Ei '' "1 s~^$~# $file~g" "$file"; # Add relative path to head of file 
    sed -Ei '' '1 s/[0-9/.]//g' "$file"; # remove digit, slash and dot of path
    sed -Ei '' '1 s/-the-//g' "$file"; # remove the first key words
    sed -Ei '' '1 s/-those-//g' "$file"; # remove those first key words
    sed -Ei '' '1 s/-/ /g' "$file"; # replace dash with space
    sed -Ei '' '1 s/md//g' "$file"; # remove md suffix
done
