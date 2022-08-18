# Re Compile Method In Python

In python, the `re.compile(r'<pattern>')` can return a matched regular pattern to a variable, to implement this pattern in the next step.

``` python
phoneRegex = re.compile(r'''( 
    (\d{3}|\(\d{3}\))? # area xxx or (xxx)
    (\s|-|\.)?   # seperator space, dash, and dot
    (\d{3})     # three number
    (\s|-|\.)    # seperator
    (\d{4})      # four number
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension space + ext or x or extsomething + space + xx-xxxxx number
    )''', re.VERBOSE)

foo = phoneRegex.search(<text>)
```

#Python #RegularExpression 
