# Search Method In Python Re Class

In re package, the `re.search(<text>)` return a group of matched pattern according to regular expresssion from the |re.compile]] method. 

``` python
>>> foo = re.compile(r'\d\D')
>>> moo = foo.search('I am 1D') # ! match 1D 
>>> moo[0]
1D
```

#Python 
