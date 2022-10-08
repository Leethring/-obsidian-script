"""find_max_words.py - Return the max number of words in note directory.

Usage Example
---
`$ python3 find_max_words.py ./Zettelkasten_note/2020/*/* ./Zettelkasten_note/2021/*/*`
"""
import os.path
import os
import sys

def count_words(lines):
    """Count the number of words of a note.
    
    Parameters
    ---
    lines: list[int]
        A list of lines in one note.
    
    Returns
    ---
    count: int
        The number of Words in one note
    """
    count = 0
    for i in lines:
        # Words split by space
        words_of_line = i.split()
        count += len(words_of_line)
    return count 

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

def find_max_words(notes):
    """Return the max number of words for given notes.
    
    Parameters
    ---
    notes: list[str] 
        A list of absolute paths of notes.

    Returns
    ---
    out: int
        The max number of words of a note from given notes.
    """
    list_count_words = []
    for note in notes:
        # Count the number of words in a note
        with open(note, 'r') as opened_note:
            lines_in_a_note = opened_note.readlines()
            count = count_words(lines_in_a_note)
            list_count_words.append(count)
    return max(list_count_words)
            
if __name__ == "__main__":
    # Read argument from command line
    system_argv = sys.argv
    note_abs_paths = find_note_path(system_argv)
    print(find_max_words(note_abs_paths))