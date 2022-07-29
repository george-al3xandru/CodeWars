# Find Nearest square number

Your task is to find the nearest square number, nearest_sq(n), of a positive integer n.

---

### Solution 1:

```python
import math

def nearest_sq(n):
    if math.sqrt(n).is_integer():
            return n
    searching = True
    m = n
    while searching:
        n += 1
        m -= 1
        if math.sqrt(n).is_integer():
            return n
        elif math.sqrt(m).is_integer():
            return m
```

### Solution 2:

```python
def nearest_sq(n):
    return round(n ** 0.5) ** 2
```
