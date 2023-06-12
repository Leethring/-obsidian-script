# Purpose: Replace `-the-` and `-` with ` ` in the note filenames and change related links
# Author: Li Weiwei
# Date: 2023-06-12
# Usage: python script.py <note files>

import os
import sys

# Find all markdown notes for name changing
note_paths = []
for i in range(len(sys.argv) - 1):
    paths = os.path.abspath(sys.argv[i + 1])
    if paths.endswith('.md'):
        note_paths.append(paths)
    else:
        continue

note_name_pairs = {}
new_note_paths = []
old_note_filenames = []
new_note_filenames = []
note_filename_count = 0
# Replace `-the-` and `-` with ` ` for each note filename
for note_path in note_paths:
    old_note_path = note_path
    old_note_path_with_dashes = note_path.replace("-the-", " ")
    new_note_path = old_note_path_with_dashes.replace("-", " ")
    os.rename(old_note_path, new_note_path)
    new_note_paths.append(new_note_path)
    # Remove old path and add new path to note paths
    # Extract the filename of a note from the path
    # For finding linked notes in note contents
    old_note_filename_md = old_note_path.split('/')[-1]
    old_note_filename = old_note_filename_md.replace(".md", "")
    new_note_filename_md = new_note_path.split('/')[-1]
    new_note_filename = new_note_filename_md.replace(".md", "")
    old_note_filenames.append(old_note_filename)
    new_note_filenames.append(new_note_filename)
    # For finding old links and replacing it with new links
    note_name_pairs[old_note_filename] = new_note_filename
    note_filename_count = note_filename_count + 1
    print("Dealt note filenames: " + str(note_filename_count))

# Find `[old filename|` in notes filenames and replace it with `[new filename|`
note_count = 0
for note_path in new_note_paths:
    with open(note_path, 'r', encoding='UTF-8') as file:
        note_contents = file.read()
        for unchanged_note_filename in old_note_filenames:
            if unchanged_note_filename in note_contents :
                note_contents \
                = note_contents.replace(unchanged_note_filename, note_name_pairs[unchanged_note_filename])
    # Write changed contents to the original note
    with open(note_path, 'w', encoding='UTF-8') as file:
         file.write(note_contents)
    note_count = note_count + 1
    print("Dealt notes: " + str(note_count))