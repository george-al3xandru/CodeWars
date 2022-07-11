# No zeros for heros

Numbers ending with zeros are boring.

They might be fun in your world, but not here.

Get rid of them. Only the ending ones.

```
1450 -> 145
960000 -> 96
1050 -> 105
-1050 -> -105
```

Zero alone is fine, don't worry about it. Poor guy anyway

---

### Solution 1:

```python
def no_boring_zeros(n):
    last_digit = n % 10
    if n == 0:
        return 0
    while last_digit == 0:
        n = n // 10
        last_digit = n % 10
    return n
```

### Solution 2:

```python
def no_boring_zeros(n):
    try:
        return int(str(n).rstrip('0'))
    except ValueError:
        return 0
```
