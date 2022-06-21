# Beginner Series # 1 School Paperwork

Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.

Your task is to calculate how many blank pages do you need.

Example:
```
n= 5, m=5: 25
n=-5, m=5:  0
```

Note: if n or m < 0 return 0

---

### Solution:

```python
def paperwork(n, m):
    if n < 0 or m < 0:
        return 0
    else:
        return n * m
```
