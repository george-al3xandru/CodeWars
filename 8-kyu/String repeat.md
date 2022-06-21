# String repeat

### Task:

Write a function called repeatStr which repeats the given string string exactly n times.

```
repeat_str(6, "I") -> "IIIIII"
repeat_str(5, "Hello") -> "HelloHelloHelloHelloHello"
```

---

### Solution:

```python
def repeat_str(repeat, string):
    new_string = ""
    for i in range(0, repeat):
        new_string += string
    return new_string
```
