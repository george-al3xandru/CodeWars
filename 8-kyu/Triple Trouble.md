# Triple Trouble

Create a function that will return a string that combines all of the letters of the three inputed strings in groups. Taking the first letter of all of the inputs and grouping them next to each other. Do this for every letter, see example below!

E.g. Input: `aa`, `bb` , `cc` => Output: `abcabc`

Note: You can expect all of the inputs to be the same length.

---

### Solution 1:

```python
def triple_trouble(one, two, three):
    string = ""
    for i in range(0, len(one)):
        string += one[i]
        string += two[i]
        string += three[i]
    return string
        
```

### Solution 2:

```python
def triple_trouble(one, two, three):
    return "".join(a+b+c for a,b,c in zip(one,two,three))
```
