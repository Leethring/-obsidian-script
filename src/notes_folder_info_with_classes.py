"""This files show all information that we want to know.

Suspended for time limit
"""
import os
import glob


class Note:
    """Notes with filenames."""

class NoteSystem():
    """Note system used by us."""
    def __init__(self, absolute_path):
        self.abspath = absolute_path
        self.files = os.listdir(self.abspath)
    
    def list_note_directories(self):
        """List all note directories in the note system"""
        directories = []
        all_file_in_my_notes = os.listdir(os.path.join(self.abspath, 'my_notes'))
        all_file_in_projects = os.listdir(os.path.join(self.abspath, 'Projects'))
        all_files = all_file_in_my_notes + all_file_in_projects
        for i in all_files:
            if '.' not in i:
                directories.append(i)
        return directories
    
    def list_notes(self):
        """List all notes in the note system."""
        notes = [] 
        for foldername, subfolders, filenames in os.walk(self.abspath):
            for filename in filenames:
                if filename.endswith('.md'):
                    notes.append(filename)
        return notes

    def create_choice(self):
        start_character_with_uppercase_a = 65
        # Create Choices
        characters_as_choices = []
        note_directories = self.list_note_directories()
        for i in range(len(note_directories)):
            characters_as_choices.append(chr(start_character_with_uppercase_a + i))
        # Create choice-folder pairs
        choice_to_chosen_folder = {}
        for i in range(len(note_directories)):
            choice_to_chosen_folder[characters_as_choices[i]] = note_directories[i]
        return choice_to_chosen_folder

    
class MyNote(NoteSystem):
    """My notes directories in note system"""
    def __init__(self, absolute_path):
        NoteSystem.__init__(self, absolute_path)
        self.abspath = os.path.join(absolute_path, 'my_notes')
        self.files = os.listdir(self.abspath)

class Projects(NoteSystem):
    """Projects directories in note system"""
    def __init__(self, absolute_path):
        NoteSystem.__init__(self, absolute_path)
        self.abspath = os.path.join(absolute_path, 'Projects')
        self.files = os.listdir(self.abspath)
    
class Interface():
    """Interface for choosing note folders"""
    def __init__(self, choice_pairs):
        self.choice = choice_pairs

    def show_choices(self):
        """Show all choices"""
        print("""
        Please choose a general folder to to inspect note directory (Input its letter):
        (Quit when typing others)
        """)
        for key, value in self.choice.items():
            print(f'{key}. {value}')
    
    def input(self):
        choice = input()
    

if __name__ == "__main__":
    absolute_path_of_note_system = '/Users/liweiwei/Nutstore Files/note_system'
    note_system = NoteSystem(absolute_path_of_note_system)
    my_note = MyNote(absolute_path_of_note_system)
    projects = Projects(absolute_path_of_note_system)
    choices = note_system.create_choice()
    interface = Interface(choices)
    interface.show_choices()