#! python3
# add_frontmatter.py - adds uid, date, and alias in the head of a notes
# Usage: python3 add_see_also_section.py /path/to/notes, such as ./wiki-note/2022/*

import os
import re
import sys

# Find all markdown notes
filenames = []
for i in range(len(sys.argv) - 1):
    files = os.path.abspath(sys.argv[i + 1])
    if files.endswith('.md'):
        filenames.append(files)
    else:
        continue

# Add See Also section 
for filename in filenames:
    with open(filename, 'r', encoding='UTF-8') as matched_filename:
        lines_of_a_file = matched_filename.readlines()
        first_line = ' '
        if len(lines_of_a_file) != 0:
            first_line = lines_of_a_file[0]
            flag_of_hash_head = first_line.startswith('# ')
        else:
            flag_of_hash_head = 0
    if flag_of_hash_head:
        print(filename)
        title_match = re.match(r"(# )(.*)", str(first_line))
        original_title = title_match.group(2)
        title = str.lower(original_title)
        uid_match = re.match(r".*((\d\d\d\d)(\d\d)(\d\d)(\d\d)(\d\d)(\d\d)).*", str(filename))
        year = uid_match.group(2)
        month = uid_match.group(3)
        day = uid_match.group(4)
        date = year + '-' + month + '-' + day
        uid = uid_match.group(1)
        back_file = filename + '.bak'
        with open(filename, 'r') as read_obj, open(back_file, 'w') as write_object:
        # Write given line to the dummy file
            write_object.write('---' + '\n')
            write_object.write('author: [Li Weiwei, Liam Lee]' + '\n')
            write_object.write('date: ' + date + '\n')
            write_object.write('uid: ' + uid + '\n')
            write_object.write('alias: ' + title + '\n')
            write_object.write('---' + '\n')
        # Read lines from original file one by one and append them to the dummy file
            for line in read_obj:
                write_object.write(line)
        # remove original file
        os.remove(filename)
        # Rename dummy file as the original file
        os.rename(back_file, filename)
