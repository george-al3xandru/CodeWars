# Remove String Spaces

### Task:

Simple, remove the spaces from the string, then return the resultant string.

---

### Solution 1:

```python
def no_space(x):
    return "".join(x.split())
```

### Solution 2:

```python
def no_space(x):
    return x.replace(' ' ,'')
```
