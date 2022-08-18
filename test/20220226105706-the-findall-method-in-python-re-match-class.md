# Findall Method In Python Re Match Class

In python, the `re.findall(<text>)` can find all matched Regex pattern in text. 

``` python
>>> foo = re.compile(r'\d{3}')
>>> ma = foo.findall('234 2333 asd333') # find matched pattern with greedy match
>>> ma
['234', '233', '333']
>>>
```

## findall() method vs search() method

The findall method search all matched pattern, and the search method only search one matched pattern. 

#Python 
