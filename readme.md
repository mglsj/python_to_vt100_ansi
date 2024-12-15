Run python code in IPython and convert it to VT100 / ANSI text

Input:

```python
marks=10
if marks>20:
    print "GODD SCORE"
```

Output:

```ansi
Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
[35m[1m>>> [0mmarks=10
[35m[1m>>> [0mif marks>20:
[35m[1m... [0m        print "GODD SCORE"
[35m[1m... [0m        
  File [35m"<python-input-1>"[0m, line [35m2[0m
    [31m[1mprint "GODD SCORE"[0m
    [31m[1m^^^^^^^^^^^^^^^^^^[0m
[35m[1mSyntaxError[0m: [35mMissing parentheses in call to 'print'. Did you mean print(...)?[0m
```
