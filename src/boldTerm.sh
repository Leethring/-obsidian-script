#! /bin/sh
# boldTerm.sh bold the original term in notes.

# for every file in argument, do the execution 
for file in "$@"; do 
    # \1 is group 1, the left display text
    sed -Ei '' 's/`([a-zA-Z0-9 #()/-]+)`/\*\*\1\*\*/g' "$file"
done


##    sed -i '' 's/\[\[.*|\(.*\)\]\]/\1/g' "$file"
# Example:
# $ sh boldTerm.sh file.md
#
# text before: `key`
# text after: **key**
