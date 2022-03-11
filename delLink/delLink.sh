#! /bin/sh
# deleteObsidianLink.sh will delete the Obsidian link of a file.

sed -i ''  's/\[\[.*|//g' $1
sed -i '' 's/\]\]//g' $1

# $ sh deleteObsidianLink.sh file.md
#
# text before: "[[1a-note-method|note method]]"
# text after: "note method"
