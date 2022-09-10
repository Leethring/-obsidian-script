# noteSystemData.py - Shows some data about our note system. 
# Include:
# Average number of new notes daily, monthly
# Max number of new notes daily, monthly
# Sum of New notes every month
import os
import glob

def walkNotes(f):
    """Counts the number of notes within a directory."""
    folderName = os.path.basename(f)
    globMonthPath = os.path.join(f, '*/*/*')
    globYearPath = os.path.join(f, '*/*')
    allMonthFiles = glob.glob(globMonthPath)
    allYearFiles = glob.glob(globYearPath)
    allFiles = allMonthFiles + allYearFiles
    notes = []
    for file in allFiles:
        if file.endswith('.md'):
            notes.append(os.path.basename(file))
    print(f'The total number of notes in this directory is:')
    return notes

def year(notes):
    """Show the number of notes within a year.
    
    notes: A list includes all notes
    """
    yearDict = {}
    startYear = 2018
    for i in range(5):
        yearDict[str(startYear + i)] = 0
    for i in range(5):
        yearCounter = 0
        for note in notes:
            if note.startswith(str(startYear+ i)):
                yearCounter = yearCounter + 1
        yearDict[str(startYear +i)] = yearCounter
    print(f'Every year include different numbers of note:\n{yearDict}\n')
    # Find the max number of adding within a year 
    maxNumNote = max(yearDict.values())
    maxYear = {i for i in yearDict if yearDict[i]==maxNumNote}
    print(f'The max number of notes a year is: {maxNumNote} in {list(maxYear)[0]} year\n')
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

def day(notes):
    """show day information of notes."""
    pass

def month(notes, yearDict):
    """Show month information about notes.
    
    show info:
        Number of notes for each month
        Max number of notes in which month 
        Average number of notes every month
    ---
    parameters:
        notes - All notes given
        yearDict - A dictionary with year-numberOfNotes pairs 
    """
    # Store all month from 2018 to 2022
    years = []
    # Add all months to each year
    for year, yearNum in yearDict.items():
        startMonth = int(str(year) + '00')
        monthsList = []
        for i in range(1, 13):
            monthsList.append(str(startMonth + i))
        years.append(monthsList)

def showYear(f):
    """Show year folders in this note directory
    
    f: Absolute path of a folder
    """
    findYear = os.path.join(f, '????')
    yearList = glob.glob(findYear)
    print('\nThis note folder include year folders:')
    for year in yearList:
        print(os.path.basename(year), end=' ')
    print("\n")

def folderInfo(f):
    """Print All information about this folder
    
    f: Absolute path of a folder
    """
    print(f'We are in folder: {os.path.basename(f)}')
    showYear(f)
    # Get all notes in a note directory
    notes = walkNotes(f)
    print(len(notes), end='\n\n')
    yearDict = year(notes)
    month(notes, yearDict)
#   day(notes)

def getPath(choice, n):
    """Return the absolute path of given folder.
    
    choice: Choice of folder name
    n: Path of note system
    """
    if choice == 'a':
        notePath = 'my_notes/zettelkasten_notes'
    elif choice == 'b':
        notePath = 'Projects/language'
    elif choice == 'c':
        notePath = 'Projects/coding'
    elif choice == 'd':
        notePath = 'my_notes/wiki-notes'
    elif choice == 'e':
        notePath = 'my_notes/creative_notes'
    notePath = os.path.join(n, notePath)
    return notePath 

def interfaceFolder():
    """Shows interface."""
    print("""
    Please choose a folder to check its information (Input its letter):
    a. Zettelkasten Directory
    b. Language Directory
    c. Coding Directory
    d. Wiki Directory 
    e. Creative Directory
    (Quit when typing others)
    """)

if __name__ == "__main__":
    noteSystemFolder = '/Users/liweiwei/Nutstore Files/note_system'
    interfaceFolder()
    folder = input()
    if folder not in 'abcde':
        quit()
    workingFolder = getPath(folder, noteSystemFolder)
    folderInfo(workingFolder)