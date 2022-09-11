#! python3
# noteSystemInfo.py - Shows information about our note system. 

import os
import glob

def day(notes):
    """Show day information of notes.
    
    Parameter
    ---
    notes (list): A list of all notes in working folder

    Variable | Show
    ---
    average_day (int): The Average number of notes every day 
        (Optimistical: days without new notes is exclusive)
    max_number (int): The Max number of notes within one day
    day_with_max (str): The day with max number
    """
    # Init a dictionary of day-note pair
    day_note_pairs = {}
    for note in notes:
        note_day_head = note[0:8]
        if note_day_head.startswith('20'):
            day_note_pairs[note_day_head] = 0
    # Count number of notes within a day
    for note in notes:
        note_day_head = note[0:8]
        if note_day_head in day_note_pairs.keys():
            day_note_pairs[note_day_head] += 1
    # Calculate average number of notes per day
    average_day =  sum(day_note_pairs.values()) // len(day_note_pairs)
    print(f'The average number of notes per note is: {average_day}')
    # Find max number of notes within a day
    max_number, day_with_max = find_max_dict_value(day_note_pairs)
    print(f'Day {day_with_max} has max number of notes: {max_number}')

def folder_info(f):
    """Print All information about this folder

    Parameters
    ---
    f: Absolute path of a folder

    Important variables | Information
    ---
    year(): Show information about year
    month(): Show information about month
    day(): Show information about day
    notes (list): A list of all notes
    """
    print(f'We are in folder: {os.path.basename(f)}')
    show_year(f)
    # Get all notes in a note directory
    notes = walk_notes(f)
    print(len(notes), end='\n\n')
    # Info about year
    year_number_dict = year(notes)
    # Info about month
    month(notes, year_number_dict)
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

def interface(p):
    """Shows interface and return a dictionary of choice-folder pair

    Parameters
    ---
    p: The absolute path of current folder

    Return
    ---
    choice_folder_pairs (dict): Dictionary of choice-folder pair
    """
    cwd_basename = os.path.basename(p)
    print(f'We are in {cwd_basename} folder')
    print("""
    Please choose a folder to check its information (Input its letter):
    (Quit when typing others)
    """)
    # Find all note folders in current folder
    my_notes = os.path.join(p, 'my_notes')
    projects = os.path.join(p, 'Projects')
    folders_in_my_notes = os.listdir(my_notes)
    folders_in_project = os.listdir(projects)
    all_folders_raw = folders_in_my_notes + folders_in_project
    folders_list = []
    # Delete folders or files not are note folders
    for i in all_folders_raw:
        if '.' not in i:
           folders_list.append(i) 
    start_char = 65
    # Create Choices
    chars = []
    for i in range(len(folders_list)):
        chars.append(chr(start_char + i))
    # Create choice-folder pairs
    choice_folder_pairs = {}
    for i in range(len(folders_list)):
        choice_folder_pairs[chars[i]] = folders_list[i]
    # Show choice of folders
    for key, value in choice_folder_pairs.items():
        print(f'{key}. {value}')
    return choice_folder_pairs

def find_max_dict_value(dict):
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
    for key, value in dict.items():
        if value > max:
            max = value
            key_with_max = key
        else:
            continue
    return max, key_with_max

def month(notes, year_number_dict):
    """Show month information about notes.

    Parameters
    ---
    notes:  All notes given
    year_number_dict:  A dictionary with year-numberOfNotes pairs 
    
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
    for year in year_number_dict.keys():
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
    max_number, maxMonth = find_max_dict_value(active_month)
    print(f'Month {maxMonth} has max number of notes: {max_number}')

def show_year(f):
    """Show year folders in this note directory
    
    Args
    ---
    f (str): Absolute path of a folder
    """
    # Every year has string of 4 digits.
    findYear = os.path.join(f, '????')
    yearList = glob.glob(findYear)
    print('\nThis note folder includes year folders:')
    for year in yearList:
        print(os.path.basename(year), end=' ')
    print("\n")

def walk_notes(f):
    """Counts the number of notes within a directory.
    
    Args:
        f: the path of this note folder
    """
    # Find all files in this folder
    notes = []
    for foldername, subfolders, filenames in os.walk(f):
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
    year_number_dict (dictionary): A dictionary of year-note pairs
        that is Returned
    max_number (int): The max number of notes within a year
    maxYear (int): The year that has max number of notes
    """
    # Dictionary to store year-numberOfNotes pairs
    year_number_dict = {}
    # We start write note from 2018 
    startYear = 2018
    # Init year dictionary
    for i in range(5):
        year_number_dict[str(startYear + i)] = 0
    # Record correct year-notes pair
    for i in range(5):
        yearCounter = 0
        for note in notes:
            if note.startswith(str(startYear+ i)):
                yearCounter = yearCounter + 1
        year_number_dict[str(startYear +i)] = yearCounter
    print(f'Every year include different numbers of note:\n{year_number_dict}\n')
    # Show the max number of adding within a year 
    max_number = max(year_number_dict.values())
    maxYear = {i for i in year_number_dict if year_number_dict[i]==max_number}
    print(f'Year {list(maxYear)[0]} has max number of notes: {max_number}')
    # Calculate average notes of this year
    yearSum = 0
    yearAverage = 0
    # When a year don't have any notes, we don't average this year
    countYear = 0
    for value in year_number_dict.values():
        if value == 0:
            continue
        else:
            yearSum += value
            countYear += 1
    yearAverage = yearSum // countYear
    print(f'The average of adding notes every year is: {yearAverage}\n')
    return year_number_dict

if __name__ == "__main__":
    note_system_folder = '/Users/liweiwei/Nutstore Files/note_system'
    # Show the interface
    choices = interface(note_system_folder)
    # Input the folder you want to know
    choice_lowercase = input()
    choice = choice_lowercase.upper()
    if choice not in choices.keys():
        quit()
    print(f'You have chosen {choice}. {choices[choice]}')
    # Store the chosen folder 
    working_folder = getPath(choices[choice], note_system_folder)
    # Show all information about a note folder.
    folder_info(working_folder)