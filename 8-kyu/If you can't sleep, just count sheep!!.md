# If you can't sleep, just count sheep!!

### Task:

Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...".

Input will always be valid, i.e. no negative integers.

---

### Solution 1:

```python
def count_sheep(n):
    s = ""
    for i in range(1, n+1):
        s += f"{i} sheep..."
    return s
```

### Solution 2:

```python
def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1,n+1))
```
