# Returning Strings

Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".

---

### Solution 1:

```python
def greet(name):
    return f'Hello, {name} how are you doing today?'
```

### Solution 2:

```python
def greet(name):
    return "Hello, {} how are you doing today?".format(name)
```
