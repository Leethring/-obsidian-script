# Docstrings Of Python

In python, The `docstrings` is the first documenting block of a code entity (class, method, attribute, etc.), that describes the information about this code entity to help users understand its usage. It is bracketed by triple-double quote  `"""<docstrings>"""`. 

When we don't understand a class or a method, we can use help() method to access useful information which show the dostrings of this method. 

## Code Example

``` python
class exampleDocstrings:
	""" This is a example to describe the exampleDosstrings class in one line

	Separated by a blank line, we can have more detailed information about this class
	-----
	Attribute: we can have attributes for this class
	-----
	Method: use method to operate data and variable. 
	--- 
	"""
	def exampleMethod():
		""" this is a method docstrings """
		pring("print a string.")
```

## See Also 

#Python 
