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
    averDay (int): The Average number of notes every day 
        (Optimistical: days without new notes is exclusive)
    maxNum (int): The Max number of notes within one day
    maxDay (str): The day with max number
    """
    # Init a dictionary of day-note pair
    daysNotes = {}
    for note in notes:
        noteDayHead = note[0:8]
        if noteDayHead.startswith('20'):
            daysNotes[noteDayHead] = 0
    # Count number of notes within a day
    for note in notes:
        noteDayHead = note[0:8]
        if noteDayHead in daysNotes.keys():
            daysNotes[noteDayHead] += 1
    # Calculate average number of notes per day
    averDay =  sum(daysNotes.values()) // len(daysNotes)
    print(f'The average number of notes per note is: {averDay}')
    # Find max number of notes within a day
    maxNum, maxDay = maxDict(daysNotes)
    print(f'Day {maxDay} has max number of notes: {maxNum}')

def folderInfo(f):
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
    showYear(f)
    # Get all notes in a note directory
    notes = walkNotes(f)
    print(len(notes), end='\n\n')
    # Info about year
    yearDict = year(notes)
    # Info about month
    month(notes, yearDict)
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
    myNotesAbs = os.path.join(path, 'my_notes')
    projectsAbs = os.path.join(path, 'Projects')
    myNotesFolders = os.listdir(myNotesAbs)
    # Return absolute path of the chosen folder
    if choice in myNotesFolders:
        return os.path.join(myNotesAbs, choice)
    else:
        return os.path.join(projectsAbs, choice)

def interfaceFolder(p):
    """Shows interface and return a dictionary of choice-folder pair

    Parameters
    ---
    p: The absolute path of current folder

    Return
    ---
    dirDict (dict): Dictionary of choice-folder pair
    """
    cwdBasename = os.path.basename(p)
    print(f'We are in {cwdBasename} folder')
    print("""
    Please choose a folder to check its information (Input its letter):
    (Quit when typing others)
    """)
    # Find all note folders in current folder
    my_notes = os.path.join(p, 'my_notes')
    projects = os.path.join(p, 'Projects')
    dirListMyNotes = os.listdir(my_notes)
    dirListProjects = os.listdir(projects)
    dirListRaw = dirListMyNotes + dirListProjects
    dirList = []
    # Delete folders or files not are note folders
    for i in dirListRaw:
        if '.' not in i:
           dirList.append(i) 
    startChar = 65
    # Create Choices
    listChar = []
    for i in range(len(dirList)):
        listChar.append(chr(startChar + i))
    # Create choice-folder pairs
    dirDict = {}
    for i in range(len(dirList)):
        dirDict[listChar[i]] = dirList[i]
    # Show choice of folders
    for key, value in dirDict.items():
        print(f'{key}. {value}')
    return dirDict

def maxDict(dict):
    """Return max value and related key within a dictionary.
    
    Parameters
    ---
    dict (dict): A dictionary contains values

    Returns
    ---
    max (int): The max value among dictionary's values.
    maxKey (str): The key that contains the max value.
    """
    # Find max number of adding notes in which month
    max = 0
    maxKey = 'a'
    for key, value in dict.items():
        if value > max:
            max = value
            maxKey = key
        else:
            continue
    return max, maxKey

def month(notes, yearDict):
    """Show month information about notes.

    Parameters
    ---
    notes:  All notes given
    yearDict:  A dictionary with year-numberOfNotes pairs 
    
    Variables | Show
    ---
    averMonth: Average number of notes every month
    activeMondict: Dictionary include month-note pairs (zero-note month is exclusive)
    max: Max number of notes in which month 
    maxKey: Month with max number 
    """
    # Store all month from 2018 to 2022
    years = []
    # Add all months to each year
    for year in yearDict.keys():
        startMonth = int(str(year) + '00')
        monthsList = []
        for i in range(1, 13):
            monthsList.append(str(startMonth + i))
        # years is a 2-D list
        years.append(monthsList)
    monthDict = {}
    # Create a dictionary that shows month-number pairs
    for year in years:
        for month in year:
            monthCount = 0
            for note in notes:
                if note.startswith(month):
                    monthCount += 1
            monthDict[str(month)] = monthCount
    # Remove month with zero note
    activeMonDict = {}
    for m, n in monthDict.items():
        if n == 0:
            continue
        else:
            activeMonDict[m] = n
    print('The months that include notes:')
    print(activeMonDict)
    # Find average of adding notes monthly
    numNote = len(notes)   
    numMonth = len(activeMonDict)
    averMonth = numNote // numMonth
    print(f'\nThe average of adding notes monthly is {averMonth}')
    # Find max number of adding notes in which month
    maxNum, maxMonth = maxDict(activeMonDict)
    print(f'Month {maxMonth} has max number of notes: {maxNum}')

def showYear(f):
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

def walkNotes(f):
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
    yearDict (dictionary): A dictionary of year-note pairs
        that is Returned
    maxNum (int): The max number of notes within a year
    maxYear (int): The year that has max number of notes
    """
    # Dictionary to store year-numberOfNotes pairs
    yearDict = {}
    # We start write note from 2018 
    startYear = 2018
    # Init year dictionary
    for i in range(5):
        yearDict[str(startYear + i)] = 0
    # Record correct year-notes pair
    for i in range(5):
        yearCounter = 0
        for note in notes:
            if note.startswith(str(startYear+ i)):
                yearCounter = yearCounter + 1
        yearDict[str(startYear +i)] = yearCounter
    print(f'Every year include different numbers of note:\n{yearDict}\n')
    # Show the max number of adding within a year 
    maxNum = max(yearDict.values())
    maxYear = {i for i in yearDict if yearDict[i]==maxNum}
    print(f'Year {list(maxYear)[0]} has max number of notes: {maxNum}')
    # Calculate average notes of this year
    yearSum = 0
    yearAverage = 0
    # When a year don't have any notes, we don't average this year
    countYear = 0
    for value in yearDict.values():
        if value == 0:
            continue
        else:
            yearSum += value
            countYear += 1
    yearAverage = yearSum // countYear
    print(f'The average of adding notes every year is: {yearAverage}\n')
    return yearDict

if __name__ == "__main__":
    noteSystemFolder = '/Users/liweiwei/Nutstore Files/note_system'
    # Show the interface
    choices = interfaceFolder(noteSystemFolder)
    # Input the folder you want to know
    choiceLow = input()
    choice = choiceLow.upper()
    if choice not in choices.keys():
        quit()
    print(f'You have chosen {choice}. {choices[choice]}')
    # Store the chosen folder 
    workingFolder = getPath(choices[choice], noteSystemFolder)
    # Show all information about a note folder.
    folderInfo(workingFolder)