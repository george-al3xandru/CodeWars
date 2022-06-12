# DESCRIPTION:
# altERnaTIng cAsE <=> ALTerNAtiNG CaSe
# altERnaTIng cAsE <=> ALTerNAtiNG CaSe
# Define String.prototype.toAlternatingCase (or a similar function/method such as to_alternating_case/toAlternatingCase/ToAlternatingCase in your selected language; see the initial solution for details) such that each lowercase letter becomes uppercase and each uppercase letter becomes lowercase. For example:

# "hello world".toAlternatingCase() === "HELLO WORLD"
# "HELLO WORLD".toAlternatingCase() === "hello world"
# "hello WORLD".toAlternatingCase() === "HELLO world"
# "HeLLo WoRLD".toAlternatingCase() === "hEllO wOrld"
# "12345".toAlternatingCase() === "12345" // Non-alphabetical characters are unaffected
# "1a2b3c4d5e".toAlternatingCase() === "1A2B3C4D5E"
# "String.prototype.toAlternatingCase".toAlternatingCase() === "sTRING.PROTOTYPE.TOaLTERNATINGcASE"
# As usual, your function/method should be pure, i.e. it should not mutate the original string.

# Solution 1
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
  
# Solution 2
def to_alternating_case(string):
    return string.swapcase()
  
# Solution 3
def to_alternating_case(string):
    return ''.join([i.upper() if i.islower() else i.lower() for i in string])
