# Enumerable Magic #20 - Cascading Subsets

Create a method each_cons that accepts a list and a number n, and returns cascading subsets of the list of size n, like so:

```
each_cons([1,2,3,4], 2)
  #=> [[1,2], [2,3], [3,4]]
```

```
each_cons([1,2,3,4], 3)
  #=> [[1,2,3],[2,3,4]]
```

As you can see, the lists are cascading; ie, they overlap, but never out of order.

---

### Solution 1:

```python
def each_cons(lst, n):
    new_list = []
    for i in range(len(lst)):
        if len(lst) - i >= n:
            x = slice(i, i + n)
            new_list.append(lst[x])
    return new_list
```

### Solution 2:

```python
def each_cons(lst, n):
    return [lst[i:i+n] for i in range(len(lst) - n + 1)]
```
