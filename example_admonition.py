"""
This program change example lines to example admonition.
"""
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

def replace_example(notes):
    """Replace example lines to example admonition
    
    Parameters
    ---
    notes: list[str] 
        A list of absolute paths of notes.

    Operation
    ---
        Replace all examples to example admonitions
    """
    for note in notes:
        for line in fileinput.input(note, inplace=1):
            if line.startswith('Example:') or line.startswith('example:'):
                line = line.replace('Example:', '> [!example]')
                line = line.replace('example:', '> [!example]')
            if line.startswith('-'):
                line = line.replace('- ', '> - ')
            sys.stdout.write(line)



if __name__ == "__main__":
    notes = find_note_path(sys.argv)
    print(notes)
    replace_example(notes)