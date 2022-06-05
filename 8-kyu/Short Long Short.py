# Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty ( zero length ).

# For example: (Input1, Input2) --> output
# ("1", "22") --> "1221"
# ("22", "1") --> "1221"

# Solution 1
def solution(a, b):
    return "".join(f"{a}{b}{a}" if len(a)<len(b) else f"{b}{a}{b}")

# Solution 2
def solution(a, b):
  return a+b+a if len(a)<len(b) else b+a+b
