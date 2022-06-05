# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# Examples (Input -> Output):
# "String"      -> "SSttrriinngg"
# "Hello World" -> "HHeelllloo  WWoorrlldd"
# "1234!_ "     -> "11223344!!__  "

# Solution 1
def double_char(s):
    new_string = ""
    for i in s:
        new_string += 2 * i
    return new_string
  
# Solution 2
def double_char(s):
    return ''.join(i * 2 for i in s)
