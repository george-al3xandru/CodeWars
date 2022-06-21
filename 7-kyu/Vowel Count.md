# Vowel Count

Task:

Return the number (count) of vowels in the given string.

We will consider `a, e, i, o, u` as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.

---

### Solution 1:

```python
def get_count(sentence):
    vowels = ["a", "e", "i", "o", "u"]
    sum = 0
    for i in range(len(vowels)):
        count = sentence.count(vowels[i])
        sum += count
    return sum
```

### Solution 2:

```python
def get_count(sentence):
    return sum(v in 'aeiou' for v in sentence)
```
