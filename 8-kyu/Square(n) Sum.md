# Square(n) Sum

### Task:

Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example:

```
for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.
```

---

### Solution 1:

```python
def square_sum(numbers):
    sum = 0
    for i in numbers:
        sum += i ** 2
    return sum
```

### Solution 2:

```python
def square_sum(numbers):
    return sum(x ** 2 for x in numbers)
```
