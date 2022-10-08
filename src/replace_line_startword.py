"""
This program change example lines to example admonition.
"""
from lib2to3.pgen2.token import NEWLINE
import os, sys
import fileinput

def find_note_path(system_argv):
    """Return a list of paths of notes
    
    Parameters
    ---
    system_argv: list[str]

    Returns
    ---
    note_abs_paths: list[str]
        A list of absolute paths of related notes
    """
    note_abs_paths = []
    for i in range(len(system_argv) - 1):
        file = os.path.abspath(system_argv[i + 1])
        # Find notes
        if file.endswith('.md'):
            note_abs_paths.append(file)
        else:
            continue
    return note_abs_paths

def replace_line(notes, old_line, new_line):
    """Replace old line to new line.
    
    Parameters
    ---
    notes: list[str] 
        A list of absolute paths of notes.
    old_line: str
        A line needed to be replaced
    new_line: str
        A line replacing the old line

    Operation
    ---
        Replace old line to new line
    """
    for note in notes:
        for line in fileinput.input(note, inplace=1):
            if line.startswith(old_line):
                line = line.replace(old_line, new_line)
            sys.stdout.write(line)

if __name__ == "__main__":
    notes = find_note_path(sys.argv)
    old_line = '例：'
    new_line = '> [!example] 例'
    replace_line(notes, old_line, new_line)