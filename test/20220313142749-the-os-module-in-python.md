# os module

In python, the `os` module is a operating system interface. 

``` python 
import os
```


## chdir()

`os.chdir(<path>)` change current working directory to the given path.

``` python
>>> os.chdir('Temporary')
'/Users/liweiwei/Temporary'
```

## getcwd()

The `os.getcwd()` can return current work directory

``` python
>>> os.getcwd()
'/home/liweiwei/'
```

## listdir()

`os.listdir(<path>)` function list all files and folders in current working directory with list data type

``` Python 
>>> os.listdir('.')
['test', 'test.md', '1.md']
```

## makedirs()

`os.makedirs(<pathname>)`  create a new directory
``` python
In [7]: os.makedirs('foo') # create a foo directory in current work directory
In [9]: os.makedirs('/users/liweiwei/Temporary/test/foo')
# create a foo directory in test directory
```

## rmdir()

`os.rmdir()` function remove a folder path.

``` python
>>> ls
testFolder anotherFolder
>>> os.rmdir('testFolder')
>>> ls
anotherFolder
```

## unlink()

`os.unlink(<path>)` function unlinks (remove) a file from given path. 

``` python
>>> ls
test.md test.txt
>>> os.unlink('test.md')
test.txt
```

## walk()

`os.walk(<path>)` method walk the whole tree of given path return a tuple including a list of foldername, a list of subfoler, a list of files in folder. 
``` Python
for foldername, subfolders, filenames in os.walk('.'):
	print(foldername)
	for subfolder in subfolders:
		print(subfolder)
	for filename in filenames:
		print(filename)
```

## See Also

#Python 