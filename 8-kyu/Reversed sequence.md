# Reversed sequence

Build a function that returns an array of integers from n to 1 where n>0.

Example : 

```
n=5 --> [5,4,3,2,1]
```

---

### Solution 1:

```python
def reverse_seq(n):
    arr = []
    for i in range(n):
        arr.append(n-i)
    return arr
```

### Solution 2:

```python
def reverse_seq(n):
    return list(range(n, 0, -1))
```

### Solution 3:

```python
def reverses_eq(n):
    return [i for i in range(n, 0, -1)]
```
