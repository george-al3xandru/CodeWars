# Beginner - Reduce but Grow

Given a non-empty array of integers, return the result of multiplying the values together in order.

Example:

```
[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
```

---

### Solution:

Python:

```python
def grow(arr):
    result = 1
    for i in arr:
        result *= i
    return result
```

JavaScript:

```javascript
function grow(x){
  return x.reduce((acc, elem) => acc * elem, 1);
}
```
