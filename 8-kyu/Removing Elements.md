# Removing Elements

### Task:

Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

Example:

```
["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]
```

None of the arrays will be empty, so you don't have to worry about that!

---

### Solution 1:

```python
def remove_every_other(my_list):
    i = 1
    while i < len(my_list):
        my_list.pop(i)
        i += 1
    return my_list
```

### Solution 2:

```python
def remove_every_other(my_list):
    return my_list[::2]
```
