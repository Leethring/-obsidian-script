#! python3
# addSeeAlso.py - Adds See Also section at the end of a note

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

# Add See Also section 
for filename in filenames:
    # Check if a note has a tag
    with open(filename, 'r') as matchF:
        matchLine = matchF.readlines()
        haveTag = re.findall('#[a-zA-Z]', str(matchLine))
        haveSA = re.findall('## See Also?', str(matchLine))
    # Add new section if notes have a tag
    if bool(haveSA):
        continue
    if bool(haveTag):
        with open(filename, 'r') as f:
            lines_ori = f.readlines()
            lines_del = lines_ori[:-2] # Delete last two lines
        with open(filename, 'w') as f_w:
            for i in lines_del:
                f_w.write(i)
            f_w.write('\n## See Also \n')
            f_w.write(lines_ori[-2]) # Add back last two lines
            f_w.write(lines_ori[-1])
    else:
        # If a note doesn't have a See Also section and tags
        # directly add the See Also section
        with open(filename, 'a') as file_also:
            file_also.write('\n\n## See Also \n')