# Super Duper Easy

Make a function that returns the value multiplied by 50 and increased by 6. If the value entered is a string it should return "Error".

---

### Solution 1:

```python
def problem(a):
    try:
        return a * 50 + 6
    except TypeError:
        return "Error"
```

### Solution 2:

```python
def problem(a):
    return "Error" if isinstance(a, str) else a * 50 + 6
```
