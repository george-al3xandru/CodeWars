# Isograms

An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

```
"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)
```

---

### Solution 1:

```python
def is_isogram(string):
    lower_string = string.lower()
    for i in lower_string:
        x = 0
        x = lower_string.count(i)
        if x > 1:
            return False
    else:
        return True
```

### Solution 2:

```python
def is_isogram(string):
    lower_string = string.lower()
    return len(lower_string) == len(set(lower_string))
```
