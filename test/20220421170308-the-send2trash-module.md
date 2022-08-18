# send2trash module

`send2trash` module send file to the trash bin of this computer folder system.

``` python
>>> import send2trash
>>> send2trash.send2trash('test.md')
# the test.md is sent to the trash
```

## send2trash method vs other remove method

Files sent to the trash can be find back from the trash bin. However, `os.unlink()`, `os.rmdir()`,  `os.rmtree()` remove files or folders forever. 