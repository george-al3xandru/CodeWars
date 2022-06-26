# Mumbling

This time no story, no theory. The examples below show you how to write function `accum`:

Examples:

```
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
```

The parameter of accum is a string which includes only letters from `a..z` and `A..Z`.

---

### Solution 1

```python
def accum(s):
    list = []
    for i, n in enumerate(s):
        string = ""
        for j in range(0, i + 1):
            string += n
        list.append(string.capitalize())    
    return "-".join(list)
```

### Solution 2:

```python
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
```
