"""
noteSystemInfo.py - Shows information about our note system. 

Information about day, month, and year are showed. 
At the start, a note folder needed to chosen to show related information 
"""

import os
import glob

def day(notes):
    """Show day information of notes.

    This function shows the average number of notes every day, 
    the max number of notes within a day, the day with the max number.
    
    Parameter
    ---
    notes (list): A list of all notes in working folder

    Variable | Show
    ---
    average_num_per_day (int): The Average number of notes every day 
        (Optimistical: days without new notes is exclusive)
    max_number (int): The Max number of notes within one day
    day_with_max (str): The day with max number
    """
    # Init a dictionary of day-note pair
    day_to_notes = {}
    for note in notes:
        # The first 8 characters of a note is a unique day
        unique_day = note[0:8]
        if unique_day.startswith('20'):
            day_to_notes[unique_day] = 0
    # Count number of notes within a day
    for note in notes:
        unique_day = note[0:8]
        if unique_day in day_to_notes.keys():
            day_to_notes[unique_day] += 1
    # Calculate average number of notes per day
    average_num_per_day =  sum(day_to_notes.values()) // len(day_to_notes)
    print(f'The average number of notes per note is: {average_num_per_day}')
    # Find max number of notes within a day
    max_number, day_with_max = find_max_value(day_to_notes)
    print(f'Day {day_with_max} has max number of notes: {max_number}')

def folder_info(absolute_path_of_folder):
    """Print All information about this folder

    Parameters
    ---
    absolute_path_of_folder: Absolute path of a folder

    Important variables | Information
    ---
    year(): Show information about year
    month(): Show information about month
    day(): Show information about day
    notes (list): A list of all notes
    """
    print(f'We are in folder: {os.path.basename(absolute_path_of_folder)}')
    show_year(absolute_path_of_folder)
    # Get all notes in a note directory
    notes = walk_notes(absolute_path_of_folder)
    print(len(notes), end='\n\n')
    # Info about year
    year_to_number_of_notes = year(notes)
    # Info about month
    month(notes, year_to_number_of_notes)
    day(notes)
    print('End of all information.')

def getPath(choice, path):
    """Return the absolute path of given folder.

    Parameters
    ---
    choice: Choice of folder name
    path: Path of note system
    """
    # Find all notes folders
    my_notes_absolute_path = os.path.join(path, 'my_notes')
    projects_absolute_path = os.path.join(path, 'Projects')
    folders_in_my_notes = os.listdir(my_notes_absolute_path)
    # Return absolute path of the chosen folder
    if choice in folders_in_my_notes:
        return os.path.join(my_notes_absolute_path, choice)
    else:
        return os.path.join(projects_absolute_path, choice)

def interface(absolute_path_of_note_system):
    """Shows interface and return a dictionary of choice-folder pair

    Parameters:
        path: The absolute path of current folder

    Returns:
        choice_to_chosen_folder (dict): Dictionary of choice-folder pair
    """
    cwd_basename = os.path.basename(absolute_path_of_note_system)
    print(f'We are in {cwd_basename} folder')
    print("""
    Please choose a folder to check its information (Input its letter):
    (Quit when typing others)
    """)
    # Find all note folders in current folder
    absolute_path_of_my_notes = os.path.join(absolute_path_of_note_system, 'my_notes')
    absolute_path_of_projects = os.path.join(absolute_path_of_note_system, 'Projects')
    folders_in_my_notes = os.listdir(absolute_path_of_my_notes)
    folders_in_project = os.listdir(absolute_path_of_projects)
    all_folders_raw = folders_in_my_notes + folders_in_project
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
    return choice_to_chosen_folder

def find_max_value(dictionary_with_values):
    """Return max value and related key within a dictionary.
    
    Parameters
    ---
    dict (dict): A dictionary contains values

    Returns
    ---
    max (int): The max value among dictionary's values.
    key_with_max (str): The key that contains the max value.
    """
    # Find max number of adding notes in which month
    max = 0
    key_with_max = 'a'
    for key, value in dictionary_with_values.items():
        if value > max:
            max = value
            key_with_max = key
        else:
            continue
    return max, key_with_max

def month(notes, year_to_number_of_notes):
    """Show month information about notes.

    Parameters
    ---
    notes:  All notes given
    year_to_number_of_notes:  A dictionary with year-numberOfNotes pairs 
    
    Variables | Show
    ---
    average_month: Average number of notes every month
    activeMondict: Dictionary include month-note pairs (zero-note month is exclusive)
    max: Max number of notes in which month 
    key_with_max: Month with max number 
    """
    # Store all month from 2018 to 2022
    years = []
    # Add all months to each year
    for year in year_to_number_of_notes.keys():
        start_month = int(str(year) + '00')
        months = []
        for i in range(1, 13):
            months.append(str(start_month + i))
        # years is a 2-D list
        years.append(months)
    month_number_pairs = {}
    # Create a dictionary that shows month-number pairs
    for year in years:
        for month in year:
            count_month = 0
            for note in notes:
                if note.startswith(month):
                    count_month += 1
            month_number_pairs[str(month)] = count_month
    # Remove month with zero note
    active_month = {}
    for m, n in month_number_pairs.items():
        if n == 0:
            continue
        else:
            active_month[m] = n
    print('The months that include notes:')
    print(active_month)
    # Find average of adding notes monthly
    number_notes = len(notes)   
    number_month = len(active_month)
    average_month = number_notes // number_month
    print(f'\nThe average of adding notes monthly is {average_month}')
    # Find max number of adding notes in which month
    max_number, maxMonth = find_max_value(active_month)
    print(f'Month {maxMonth} has max number of notes: {max_number}')

def show_year(absolute_path_of_given_folder):
    """Show year folders in this note directory
    
    Args
    ---
    f (str): Absolute path of a folder
    """
    # Every year has string of 4 digits.
    findYear = os.path.join(absolute_path_of_given_folder, '????')
    yearList = glob.glob(findYear)
    print('\nThis note folder includes year folders:')
    for year in yearList:
        print(os.path.basename(year), end=' ')
    print("\n")

def walk_notes(absolute_path_of_note_folder):
    """Counts the number of notes within a directory.
    
    Args:
        f: the path of this note folder
    """
    # Find all files in this folder
    notes = []
    for foldername, subfolders, filenames in os.walk(absolute_path_of_note_folder):
        for filename in filenames:
            if filename.endswith('.md'):
                notes.append(filename)
    print(f'The total number of notes in this directory is:')
    return notes

def year(notes):
    """Show the number of notes within a year.

    Parameters:
        notes: A list includes all notes

    Returns | Variable | Info
    ---
    year_to_number_of_notes (dictionary): A dictionary of year-note pairs
        that is Returned
    max_number (int): The max number of notes within a year
    year_with_max_number (int): The year that has max number of notes
    """
    # Dictionary to store year-numberOfNotes pairs
    year_to_number_of_notes = {}
    # We start write note from 2018 
    start_year = 2018
    # Init year dictionary
    for i in range(5):
        year_to_number_of_notes[str(start_year + i)] = 0
    # Record correct year-notes pair
    for i in range(5):
        year_counter = 0
        for note in notes:
            if note.startswith(str(start_year+ i)):
                year_counter = year_counter + 1
        year_to_number_of_notes[str(start_year +i)] = year_counter
    print(f'Every year include different numbers of note:\n{year_to_number_of_notes}\n')
    # Show the max number of adding within a year 
    max_number = max(year_to_number_of_notes.values())
    year_with_max_number = {i for i in year_to_number_of_notes if year_to_number_of_notes[i]==max_number}
    print(f'Year {list(year_with_max_number)[0]} has max number of notes: {max_number}')
    # Calculate average notes of this year
    sum_of_years = 0
    average_of_years = 0
    # When a year don't have any notes, we don't average this year
    number_of_years_having_notes = 0
    for value in year_to_number_of_notes.values():
        if value == 0:
            continue
        else:
            sum_of_years += value
            number_of_years_having_notes += 1
    average_of_years = sum_of_years // number_of_years_having_notes
    print(f'The average of adding notes every year is: {average_of_years}\n')
    return year_to_number_of_notes

if __name__ == "__main__":
    absolute_path_of_note_system = '/Users/liweiwei/Nutstore Files/note_system'
    # Show the interface
    choices = interface(absolute_path_of_note_system)
    # Input the folder you want to know
    choice_lowercase_or_uppercase = input()
    choice = choice_lowercase_or_uppercase.upper()
    if choice not in choices.keys():
        quit()
    print(f'You have chosen {choice}. {choices[choice]}')
    # Store the chosen folder 
    working_folder = getPath(choices[choice], absolute_path_of_note_system)
    # Show all information about a note folder.
    folder_info(working_folder)