# String in Python 

The **string** in Python is a built-in data type.

``` Python
>>> a = 'I am a string'
```

## endswith() method

`str.endswith(<string>)` return `True` if the string object ends with given string.

``` Python
>>> a = 'I love you'
>>> a.endswith('you')
True
```


## format Method 

The `format()` method give a string template values. We use curly brace `{}` to give where the value needed to be placed. We use parenthesis `()` to include the template value.

For example, 

``` python
In [6]: a = "{0} love {1}".format("I", "you")

In [7]: a
Out[7]: 'I love you'
```

``` python
In [8]: b = "I {2} you"
In [9]: b
Out[9]: 'I {2} you'

In [10]: b.format("I", "you", "love")
Out[10]: 'I love you'
```

## join

`str.join(iterable)` return a string that include all members of iterable joined by the string object. 

The members of iterable should be string object. 

``` python
>>> a = ' '
>>> test = ['1', '2', '3']
>>> a.join(test)
'1 2 3'
```

## lower() 

`str.lower()` return lowercase of a given string. 
``` python
>>> a = 'I LOVE YOU'
>>> a.lower()
'i love you'
```

## startswith() 

`str.startswith(<string>)` return `True` if the string object starts with given string.

``` python
>>> a = 'I love you'
>>> a.startswith('I love')
True
```

