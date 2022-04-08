#! /bin/sh
# capitalizeWords.sh capitalizes the first letter of words in the first line.

for file in "$@"; do
    find $file -type f -exec gsed -i '1 s/\b\(.\)/\u\1/g' {} +
done