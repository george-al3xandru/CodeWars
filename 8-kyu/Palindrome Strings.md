# Palindrome Strings

A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward. This includes capital letters, punctuation, and word dividers.

Implement a function that checks if something is a palindrome. If the input is a number, convert it to string first.

Examples(Input ==> Output)
```
"anna"   ==> true
"walter" ==> false
12321    ==> true
123456   ==> false
```

---

### Solution 1:

```python
def is_palindrome(string):
    return str(string) == str(string)[::-1]
```

### Solution 2:

```python
def is_palindrome(string):
    string = str(string)
    left = 0
    right = len(string) - 1
    
    while left < right:
        if string[left] == string[right]:
            left += 1
            right -= 1
        else:
            return False
        
    return True
```
