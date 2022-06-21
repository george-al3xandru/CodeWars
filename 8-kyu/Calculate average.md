# Calculate average

Write a function which calculates the average of the numbers in a given list.

Note: Empty arrays should return 0.

---

### Solution:

```python
def find_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0
```
