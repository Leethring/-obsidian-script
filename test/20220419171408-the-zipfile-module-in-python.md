# Zipfile Module

The `zipfile` module include a series of operations related to ZIP file.

``` python
>>> import zipfile
```

## ZipFile Object

`zipfile.ZipFile(<Archive files>, <mode>)` return a ZipFile object, opening a ZIP file. If the ZIP file doesn't exist, create it. 

``` python
>>> foo = zipfile.ZipFile('test.zip', 'w') # Write mode
>>> type(foo)
zipfile.ZipFile
```

### mode 

There three modes for a ZipFile object, they're `'r'`, `'w'`, `'a'`, standing for *read*, *write*, *add*, respectively. For a ZIP file, the wirte mode overwrites the ZIP file with adding new files; the add mode adds new files companying with existed files. 

## ZipFile.close method

`ZipFile.close()` close a ZipFile object. If the archive process for a ZIP file, we close it.

## ZipFile.extract method

`ZipFile.extract(<file>, <destination>)` extract single file in current working directory.
``` python
>>> foo.extract('RomeoAndJuliet.txt','./test/')
'test/RomeoAndJuliet.txt'
```

## ZipFile.extractall method

`ZipFile.extractall(<path/to/destination>)` extract all members of Archive to the destination. If the destination folder doesn't exist, it will create one. 

## ZipFile.write method

`ZipFile.write(<files>, compress_type=None)` write files to the ZipFile objects.

## ZipFile.namelist method

`ZipFile.namelist()` return a list of member name of archive file. 

## ZipFile.getinfo method

`ZipFile.getinfo()` method returns a `ZipInfo` object. 

#Python 
