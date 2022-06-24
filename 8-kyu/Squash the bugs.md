# Squash the bugs

Simple challenge - eliminate all bugs from the supplied code so that the code runs and outputs the expected value. Output should be the length of the longest word, as a number.

There will only be one 'longest' word.

---

### Solution

```python
def find_longest(string):
    spl = string.split(" ")
    longest = 0
    for i in spl:
        if (len(i) > longest): 
            longest = len(i)
    return longest
```
