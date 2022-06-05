# Given an array of integers, return a new array with each value doubled.

# For example:
# [1, 2, 3] --> [2, 4, 6]

# Solution 1
def maps(a):
    for i in range(0,len(a)):
        a[i] *= 2
    return a

# Solutin 2
def maps(a):
    return [i*2 for i in a]
