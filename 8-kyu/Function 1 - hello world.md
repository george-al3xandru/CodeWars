# Function 1 - hello world

Make a simple function called greet that returns the most-famous "hello world!".

Style Points

Sure, this is about as easy as it gets. But how clever can you be to create the most creative hello world you can think of?

What is a "hello world" solution you would want to show your friends?

---

### Solution 1:

```python
def greet():
    return "hello world!"
```

### Solution 2:

```python
def greet():
    a_binary_string ="01101000 01100101 01101100 01101100 01101111 00100000 01110111 01101111 01110010 01101100 01100100 00100001"
    return "".join([chr(int(binary, 2)) for binary in a_binary_string.split(" ")])
```
