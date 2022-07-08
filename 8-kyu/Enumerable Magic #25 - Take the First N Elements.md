# Enumerable Magic #25 - Take the First N Elements

Create a function that accepts a list/array and a number n, and returns a list/array of the first n elements from the list/array.

---

### Solution 1:

```python
def take(arr,n):
    if n <= len(arr):
        return [arr[i] for i in range(0, n)]
    else:
        return arr
```

### Solution 2:

```python
def take(arr,n):
    return arr[:n]
```
