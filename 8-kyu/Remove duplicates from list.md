# Remove duplicates from list

Define a function that removes duplicates from an array of numbers and returns it as a result.

The order of the sequence has to stay the same.

---

### Solution 1:

```python
def distinct(seq):
    return list(dict.fromkeys(seq))
```

### Solution 2:

```python
def distinct(seq):
    return sorted(set(seq), key = seq.index)
```
