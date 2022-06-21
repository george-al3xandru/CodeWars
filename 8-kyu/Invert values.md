# Invert values

Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

```
invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []
```

You can assume that all values are integers. Do not mutate the input array/list.

---

### Solution 1:

```python
def invert(lst):
    x = 0
    inv_lst = []
    while x < len(lst):
        inv_lst.append(lst[x] * -1)
        x += 1
    return inv_lst
```

### Solution 2:

```python
def invert(lst):
    return [-x for x in lst]
```
