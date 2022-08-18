# shutil module

The `shutil` module provides a number of high-level operation for files, such as copying, removal, adjustment, etc.

``` python 
import shutil
```


## copy()

`shutil.copy(<source>,<destination>)` function copy a file or a folder from source to the destination. If the destination is a file, the destination file will be overwritten by the source file.

``` python
>>> shutiL.copy('test.md','test.txt')
'test.txt'
```

## copytree()

`shutil.copytree(<source>,<destination>)` function copy a folder and its tree structure to the destination. 

## move ()

`shutil.move()` method move a file or a folder from source path to the destination. If the destination folder doesn't exist, a `FileNotFoundError` exception is raised. If the destination is a file not a folder, the name of source file is changed to the name of destination. 

``` python
# shutil.move(<source>,<destination>)
>>> shutil.move('test','foo')
'foo'
>>> shutil.move('foo','./aFolder/')
'/Users/liweliwe/Temporary/aFolder/foo'
```
