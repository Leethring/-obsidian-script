# assert keyword

The `assert` statement  will raise `AssertionError` if the first argument is not True.

``` python
# assert <condition>, <error message>
>>> a = 'a'
>>> assert a == 'a', 'There is a "a"'
>>> a = 'b'
>>> assert a == 'a', 'There is a "a"'
---------------------------------------------------------------------------  
AssertionError                            Traceback (most recent call last)  
<ipython-input-233-f830693e981a> in <module>  
----> 1 assert a == 'a','there is a "a"'  
  
AssertionError: there is a "a"
```

#Python 