# Word Character In Regex

In Regex, the word character `\w` can match any alphanumric and underscore. 

`\w` is a not-word character. 

``` python
>>> foo = re.compile(r'\w{3}s')
>>> ma = foo.findall('lids and wods') # alphabeta
>>> ma
['lids', 'wods']
>>> ma = foo.findall('lids and wo_s') # underscore
>>> ma
['lids', 'wo_s']
>>> ma = foo.findall('lids and wo1s') # number 1 
>>> ma
['lids', 'wo1s']
```

#Regex 
