# ZipInfo object

`ZipInfo` object is returned by the `getinfo` method of ZipFile objects. The *ZipInfo* holds information about a member of an archive. 

``` python
>>> foo = ZipFile.getinfo()
# foo is a ZipInfo object
```

## file_size attribute 

`ZipInfo.file_size` attribute return the size of this compressed file (*ZipInfo* object)

``` python
>>> fooInfo = ZipFile.getinfo('test.txt')
>>> fooInfo.file_size
32
```

#Python