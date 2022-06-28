# Find the Remainder

Write a function that accepts two integers and returns the remainder of dividing the larger value by the smaller value.

Division by zero should return an empty value.

Examples:

```
n = 17
m = 5
result = 2 (remainder of `17 / 5`)

n = 13
m = 72
result = 7 (remainder of `72 / 13`)

n = 0
m = -1
result = 0 (remainder of `0 / -1`)

n = 0
m = 1
result - division by zero (refer to the specifications on how to handle this in your language)
```

---

### Solution 1:

```python
def remainder(a,b):
    x = min(a, b)
    y = max(a, b)
    if x == 0:
        return None
    return y % x
```

### Solution 2:

```python
def remainder(a, b):
    a, b = sorted((a, b))
    if a != 0:
        return b % a
```
