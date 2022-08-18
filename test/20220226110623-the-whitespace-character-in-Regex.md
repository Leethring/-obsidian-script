# Whitespace Character In Regex

In regular expression, the whitespace character `\s` can match any a space, a tab or carriage return in string. 

`\S` is a not-whitespace character. 

``` python
>>> foo = re.compile(r'\s \S')
>>> ma = foo.findall('1  S d  1')
>>> ma
['  S', '  1']
>>>
```

#Regex
