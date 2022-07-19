# Printing Array elements with Comma delimiters

Input: Array of elements

[`h`,`o`,`l`,`a`]

Output: String with comma delimited elements of the array in th same order.

`h,o,l,a`

---

### Solution:

```python
def print_array(arr):
    return ",".join(str(i) for i in arr)
```
