# Abbreviate a Two Word Name

Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

`Sam Harris` => `S.H`

`Patrick Feeney` => `P.F`

---

### Solution 1:

```python
def abbrev_name(name):
    initials = name[0] + "."
    for i, n in enumerate(name):
        if n == " ":
            initials += name[i+1]
    return initials.upper()
```

### Solution 2 (this can take more than 2 words):

```python
def abbrev_name(name):
    return '.'.join(i[0] for i in name.split()).upper()
```
