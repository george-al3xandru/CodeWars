# Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

# For example,

# [True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]
# The correct answer would be 17.

# Hint: Don't forget to check for bad values like null/undefined

# Solution 1
def count_sheeps(sheep):
    sheep_number = 0
    for i in sheep:
        if i:
            sheep_number += 1
    return sheep_number
  
# Solution 2
def count_sheeps(sheep):
  return sheep.count(True)