# Is the string uppercase?.md

Create a method to see whether the string is ALL CAPS.

Examples (input -> output):

```
"c" -> False
"C" -> True
"hello I AM DONALD" -> False
"HELLO I AM DONALD" -> True
"ACSKLDFJSgSKLDFJSKLDFJ" -> False
"ACSKLDFJSGSKLDFJSKLDFJ" -> True
```

---

### Solution:

```python
import string
def is_uppercase(inp):
    if  all(i in string.punctuation for i in inp):
        return True
    else:
        return inp.isupper()
```

string.punctuation contain all special characters and you can use 'all' function to check if all of the characters are special.
