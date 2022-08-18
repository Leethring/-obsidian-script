# requests module

The **requests** module is used to download web page. 

``` python
import requests
```


## get() method

`requests.get(<web url)` return a web's response. 

``` python
>>> x = requests.get('https://google.com')
>>> x.raise_for_status
<bound method Response.raise_for_status of <Response [200]>>
# Response 200 means that we request a web page successfully
```

## raise_for_status()

`Response.raise_for_status()` return a HTTPError object if there is a error in the requests process. 

After we request a webpage, we should use the this to check errors

``` python 
In [25]: test = requests.get('https://aasdfa.co')
In [26]: test.raise_for_status()  # Error
---------------------------------------------------------------------------  
HTTPError                                 Traceback (most recent call last)  
<ipython-input-26-798af17db09b> in <module>  
----> 1 test.raise_for_status()  
  
/opt/homebrew/lib/python3.9/site-packages/requests/![](file:///C:\Users\15216\AppData\Roaming\Tencent\QQTempSys\%W@GJ$ACOF(TYDYECOKVDYB.png)models.py in raise_for_status(self)  
    958  
    959         if http_error_msg:  
--> 960             raise HTTPError(http_error_msg, response=self)  
    961  
    962     def close(self):  
  
HTTPError: 502 Server Error: Bad Gateway for url: https://aasdfa.co
```