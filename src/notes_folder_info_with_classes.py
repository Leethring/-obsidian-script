"""This files show all information that we want to know.

Suspended for time limit
"""
import os
import glob


class NoteCollection():
    """Notes with filenames."""
    pass

class NoteDirectory():
    """A Note Directory with subdirectories and files."""
    def __init__(self,absolute_path):
        self.abspath = absolute_path
        self.directories = []
        self.subdirectories = []
        self.files = []
    
    def walk_note_directory(self):
        """Walk the whole note directory"""
        for foldername, subfolders, filenames in os.walk(self.abspath):
            self.directories.append(foldername)
            for subfolder in subfolders:
                self.subdirectories.append(subfolder)
            for filename in filenames:
                self.files.append(filename)

    def return_number_of_files(self):
        return len(self.files)
    
    def get_note_filenames(self):
        filenames = []
        for file in self.files:
            if file.endswith('.md'):
                filenames.append(os.path.basename(file))
        print(len(filenames)) 

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
    
def show_note_directories():
    """Show all subdirectories in this directory"""
    my_notes_directories = os.listdir('/Users/liweiwei/Nutstore Files/note_system/my_notes')
    project_directories = os.listdir('/Users/liweiwei/Nutstore Files/note_system/Projects')
    all_folders_raw = my_notes_directories + project_directories
    all_note_folders = []
    # Delete folders or files not are note folders
    for i in all_folders_raw:
        if '.' not in i:
           all_note_folders.append(i) 
    start_character_with_uppercase_a = 65
    # Create Choices
    characters_as_choices = []
    for i in range(len(all_note_folders)):
        characters_as_choices.append(chr(start_character_with_uppercase_a + i))
    # Create choice-folder pairs
    choice_to_chosen_folder = {}
    for i in range(len(all_note_folders)):
        choice_to_chosen_folder[characters_as_choices[i]] = all_note_folders[i]
    # Show choice of folders
    for key, value in choice_to_chosen_folder.items():
        print(f'{key}. {value}')
    return choice_to_chosen_folder, my_notes_directories, project_directories

def get_path(choice, choices, my_notes, projects):
    """Return the absolute path of given folder.

    Parameters
    ---
    choice: Choice of folder name
    path: Path of note system
    """
    # Find all notes folders
    foldername = choices[choice] 
    if foldername in my_notes:
        return os.path.join('/Users/liweiwei/Nutstore Files/note_system/my_notes', foldername)
    if foldername in projects:
        return os.path.join('/Users/liweiwei/Nutstore Files/note_system/Projects', foldername)

if __name__ == "__main__":
    absolute_path_of_note_system = '/Users/liweiwei/Nutstore Files/note_system'
    choices, my_notes_directories, projects_directories = show_note_directories()
    input_choice_lower = input()
    input_choice = input_choice_lower.upper()
    absolute_path_of_note_directory = get_path(input_choice, choices, my_notes_directories, projects_directories)
#    note_system_directory = NoteDirectory(absolute_path_of_note_system)
#    note_system_directory.walk_note_directory()
#    note_system_directory.get_note_filenames()