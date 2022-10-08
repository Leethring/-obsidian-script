"""
This program change example lines to example admonition.
(Delete unnecessary note paths)

Use 
---
$ python3 example_admonition.py ./language/2022/*/*.md

Old | example section
---
Example:
- Example1
- Example2

New | example admonition
---
> [!example]
> - Example1
> - Example2
"""
import os, sys
import fileinput

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
        for line in fileinput.input(note, inplace=True):
            # Find example line
            if line.startswith('Example:') or line.startswith('example:'):
                line = line.replace('Example:', '> [!example]')
                line = line.replace('example:', '> [!example]')
            if line.startswith('-'):
                line = line.replace('- ', '> - ')
            sys.stdout.write(line)

if __name__ == "__main__":
    replace_example(sys.argv[1:])