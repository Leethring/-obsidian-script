#! /bin/sh
# deleteObsidianLink.sh will delete the Obsidian link of files.
# Problem to be solved: this scrip delete the whole occurence in the same line

# for every file in argument, do the execution 
for file in "$@"; do 
    # \1 is group 1, the left display text
    sed -i '' 's/\[\[.*|\(.*\)\]\]/\1/g' "$file"
done

# Another version, this version will break the original [[]], such as picture
# for file in "$@"; do 
#    # \1 is group 1, the left display text
#    sed -Ei '' 's/\[\[[0-9a-zA-Z-]+\|//g' "$file"
#    sed -Ei '' 's/\]\]//g' "$file"
# done


# Example:
# $ sh deleteObsidianLink.sh file.md
#
# text before: "[[1a-note-method|note method]]"
# text after: "note method"
