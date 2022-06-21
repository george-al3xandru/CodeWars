# sPoNgEbOb MeMe

Remember the spongebob meme that is meant to make fun of people by repeating what they say in a mocking way?

You need to create a function that converts the input into this format, with the output being the same string expect there is a
pattern of uppercase and lowercase letters.

Example:

```
input:  "stop Making spongebob Memes!"
output: "StOp mAkInG SpOnGeBoB MeMeS!"
```

---

### Solution 1:

```python
def sponge_meme(s):
    output = ""
    for i in range(len(s)):
        if i%2==0:
            output += s[i].upper()
        else:
            output += s[i].lower()
    return output
```

### Solution 2:

```python
def sponge_meme(s):
    a = list(s)
    a[::2], a[1::2] = s[::2].upper(), s[1::2].lower()
    return ''.join(a)
```
