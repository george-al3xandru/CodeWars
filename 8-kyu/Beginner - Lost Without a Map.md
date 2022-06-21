# Beginner - Lost Without a Map

Given an array of integers, return a new array with each value doubled.

For example:

```
[1, 2, 3] --> [2, 4, 6]
```

---

### Solution 1:

```python
def maps(a):
    for i in range(0,len(a)):
        a[i] *= 2
    return a
```

### Solution 2:

```python
def maps(a):
    return [i*2 for i in a]
```
