import fileinput 
import sys
for line in fileinput.input('test2.txt', inplace=True):
    if line.startswith('Example:'):
        line = line.replace('Example:', '[!example]')
    print(line,end='')