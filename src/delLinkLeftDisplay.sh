#! /bin/sh
# delLinkLeftDisplay.sh delete the Obsidian link of files leaving the display text.

# for every file in argument, do the execution 
for file in "$@"; do 
    # \1 is group 1, the left display text
    gsed -i 's/\[\[[0-9a-zA-Z-]*|/\|/g' "$file"
    gsed -i 's/|\([0-9a-zA-Z ]*\)\]\]/\1/g' "$file"
done

# Example:
# $ sh delLinkLeftDisplay.sh file.md
#
# text before: "[[1a-note-method|note method]]"
# text after: "note method"
