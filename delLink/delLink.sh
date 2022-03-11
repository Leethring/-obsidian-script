#! /bin/sh
# deleteObsidianLink.sh will delete the Obsidian link of files.

# for every file in argument, do the execution 
for file in "$@"; do 
    # \1 is group 1, the left display text
    sed -i '' 's/\[\[.*|\(.*\)\]\]/\1/g' "$file"
done


# Example:
# $ sh deleteObsidianLink.sh file.md
#
# text before: "[[1a-note-method|note method]]"
# text after: "note method"
