# logging module

The `logging` module provide a flexible event logging system for applications and libraries. 

``` Python
import logging
# If we want to use the logging module, we shoud configurate it at the start of script
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
```

## debug() function 

`logging.debug(<debug message>)` shows teh debug message. 

``` python
>>> logging.debug('show the debug message')
 2022-05-17 14:08:25,569 - DEBUG - show the debug message
```

## disable function

`logging.disable(level=CRITICAL)` disables the logging message under the given level. 