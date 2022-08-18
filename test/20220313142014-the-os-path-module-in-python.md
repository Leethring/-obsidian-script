# os.path module

In python, the `os.path` module can manipulate the pathname.

## os.path.exists() method

`os.path.exists(<path>)` function returns `True` is the pathname exists. 

``` python
In [25]: os.path.exists('/users/liweiwei/')
Out[25]: True
```

## abspath

`os.path.abspath(<path>)`  return a absolute path of given path. 

``` python
In [11]: os.path.abspath('.')
Out[11]: '/Users/liweiwei/Temporary'
```

## basename

`os.path.basename()` method return a `base name` of given path

``` python
In [3]: os.path.basename('/Users/liweiwei/Temporary')
Out[3]: 'Temporary'

```

## dirname

`os.path.dirname(<path>)` return the directory name of given path.

``` python
In [3]: os.path.dirname('/Users/liweiwei/Temporary')
Out[3]: '/Users/liweiwei/'
```

## isabs

`os.path.isabs()` method return `True` if given path is a absolute path. 

``` python
In [5]: os.path.isabs('/users/liweiwei/Temporary/')
Out[5]: True
```

## join

`os.path.join(<path>,*<paths>` return a joined path from the left to the right. 

``` python
>>> os.path.join('/','Users','liweiwei')
'/Users/liweiwei'
>>> os.path.join('/','Users','/liweiwei')
'/liweiwei'
```

#Python
