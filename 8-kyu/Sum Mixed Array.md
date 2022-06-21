# Sum Mixed Array

Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

Return your answer as a number.

---

### Solution 1:

```python
def sum_mix(arr):
    sum = 0
    for i in arr:
        sum += int(i)
    return sum
```

### Solution 2:

```python
def sum_mix(arr):
    return sum(int(i) for i in arr)
```
