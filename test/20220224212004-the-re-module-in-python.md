# re Module 

In python, when we want to use regular expression we should first import a `re` module to do teh operation of regular expression. 

``` python
>>> import re
```

## module contents

### flags 

#### re.VERBOSE

The `VERBOSE` flag allow us write a nicer regular expression by seperating the pattern line by line with comments. 

``` python
test = re.compile(r'''
	20\d\d- # year
	(0|1)\d- # month
	(0|1|2|3)\d- # day
	```, re.VERBOSE)
```

### functions

#### re.complie()

`re.compile(<pattern>, flag=0)`

The `re.complie()` return a regular expression object. 

``` python
>>> test = re.compile(r'<Regex>')
# Now the test is a re.Pattern object
```

#Python 
