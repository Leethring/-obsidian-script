# File Object in python


In python, a `file object` is created by the `open()` function. When we want to operate the file object, we will use some method about file object, such `write()`, `read()`. 

``` python
>>> test = open('foo.md')
# Now test is a file object. 
```

## write() method

For a file object, `write()` can add a stream text into a file according to its mode. 

``` python
# Test is a file object in w mode
>>> test = open('foo.md','w')
>>> test.write('This is a foo file')
18 # the number of characters of string
# At the start of foo.md, "This is a foo file" is shown. 
```

## read

For a file object, `read()` method return a stream text to the I/O

``` python
>>> test = open('foo.md')
>>> test.read()
'This is a foo file'
```

## close

After we've done with the opened file, we should close it to prevent error. 

``` python
>>> test = open('test.md')
>>> test.close()
```

#Python 
