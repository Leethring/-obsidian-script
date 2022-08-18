# Group Method Of Python Re Match

In python, the `group()` method can show the matched groups of a string for a regular expression. 

In regular expression every group is divided by parentheses `()`

``` python
>>> m = re.match(r'(\w+) (\w+)', 'Feynman Richard, I')
>>> m.group(1) # group 0 store the whole matched string. 
Feynman
>>> m.group(2)
Richard
```

#Python #RegularExpression 
