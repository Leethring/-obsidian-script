#! /bin/sh
# deleteObsidianLink.sh will delete the Obsidian link of a file.

sed -i ''  's/\[\[.*|//g' $1
sed -i '' 's/\]\]//g' $1
