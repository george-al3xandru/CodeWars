# Grasshopper - Combine strings

Create a function named (`combine_names`) that accepts two parameters (first and last name). The function should return the full name.

Example:

```
combine_names('James', 'Stevens')
```

returns:

```
'James Stevens'
```

---

### Solution 1:

```python
def combine_names(first_name, last_name):
    return f"{first_name} {last_name}"
```

### Solution 2:

```python
def combine_names(*args):
    return ' '.join(args)
```
