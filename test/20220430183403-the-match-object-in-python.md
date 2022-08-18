# Match object

The `re.Match` objects have the properties of mathed string from from the search methods of [[20220430175932-the-regular-expression-objects-in-python|Pattern objects]]. If no matched pattern was returned, search method return `None`. 

``` python
# test is Pattern object with 
>>> testA = test.search('')
```

## group() method

`Match.group(number)` return the string related to the capturing group. 