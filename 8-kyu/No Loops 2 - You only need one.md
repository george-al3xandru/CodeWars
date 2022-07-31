# No Loops 2 - You only need one

*** No Loops Allowed ***

You will be given an array (a) and a value (x). All you need to do is check whether the provided array contains the value, without using a loop.

Array can contain numbers or strings. X can be either. Return true if the array contains the value, false if not. With strings you will need to account for case.

---

### Solution 1:

```python
def check(a, x): 
    if x in a:
        return True
    else:
        return False
```

### Solution 2:

```python
def check(a, x): 
    return x in a
```
