import os
import re
import sys

# Find all markdown notes
filenames = []
for i in range(len(sys.argv) - 1):
    file = os.path.abspath(sys.argv[i + 1])
    if file.endswith('.md'):
        filenames.append(file)
    else:
        continue

print(filenames)