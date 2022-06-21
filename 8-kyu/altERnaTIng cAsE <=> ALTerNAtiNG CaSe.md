# altERnaTIng cAsE <=> ALTerNAtiNG CaSe

altERnaTIng cAsE <=> ALTerNAtiNG CaSe
altERnaTIng cAsE <=> ALTerNAtiNG CaSe

Define `to_alternating_case` such that each lowercase letter becomes uppercase and each uppercase letter becomes lowercase. For example:

```
to_alternating_case("hello world") == "HELLO WORLD"
to_alternating_case("HELLO WORLD") == "hello world"
to_alternating_case("hello WORLD") == "HELLO world"
to_alternating_case("HeLLo WoRLD") == "hEllO wOrld"
to_alternating_case("12345") == "12345" // Non-alphabetical characters are unaffected
to_alternating_case("1a2b3c4d5e") == "1A2B3C4D5E"
to_alternating_case("String.prototype.toAlternatingCase") == "sTRING.PROTOTYPE.TOaLTERNATINGcASE"
```

As usual, your function/method should be pure, i.e. it should not mutate the original string.

---

### Solution 1:

```python
def to_alternating_case(string):
    new_string = ""
    for i, n in enumerate(string):
        if n.isupper():
            new_string += string[i].lower()
        elif n.islower():
            new_string += string[i].upper()
        else:
            new_string += n
    return new_string
```

### Solution 2:

```python
def to_alternating_case(string):
    return string.swapcase()
```

### Solution 3:

```python
def to_alternating_case(string):
    return ''.join([i.upper() if i.islower() else i.lower() for i in string])
```
