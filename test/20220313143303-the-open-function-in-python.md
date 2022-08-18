# Open()

`open(file,mode='r')`

In python, the `open` function can open a file and return a file object.  If the file doesn't exist, the open function create it automatically. 

``` python
>>> open('foo.md')
<_io.TextIOWrapper name='foo.md' mode='r' encoding='UTF-8'>
# defualt mode is read mode
```

## mode

The **mode** is optional string that specifies the mode in which the file is opened. The defualt mode is `'r'` mode which means open for reading in text mode. 

### write mode

`open(<file>, 'w')` 

The open function in **write mode** open a writable file for operating it. This operation will rewrite all content in the opened file.

``` python
>>> open('foo.md','w')
<_io.TextIOWrapper name='foo.md' mode='w' encoding='UTF-8'>
```

### append mode 

`open(<file>, 'a')` 

The open function in **append mode** appends plaintext at the end of a file. 

### binary mode

`'b'` specifies the binary mode for the opened file object, it is used in pictures, videos, webs, etc. 

#Python 
