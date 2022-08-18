# callstack

The **callstack** show the exception error from the bottom to the up as a form of stack showing the thread of wrong code when python interpreter work unsuccessfully. 

``` python
Traceback (most recent call last):  
  File "/Users/liweiwei/Desktop/test.py", line 7, in <module>  
    spam()  
  File "/Users/liweiwei/Desktop/test.py", line 2, in spam  
    foo()  
  File "/Users/liweiwei/Desktop/test.py", line 5, in foo  
    raise Exception('This is the error message.')  
Exception: This is the error message.
```

#Python