# Complete the solution so that it reverses the string passed into it.

# 'world'  =>  'dlrow'
# 'word'   =>  'drow'

# Solution
def solution(string):
    return string[::-1]
  
# Solution 2
def solution(string):
    new_string=""
    for x in string:
        new_string = x + new_string
    return new_string
