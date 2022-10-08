import fileinput 
import sys
for line in fileinput.input():
    print(line, end='')