# DESCRIPTION:
# Complete the function which converts a binary number (given as a string) to a decimal number.

# Solution 1
def bin_to_decimal(inp):
    return sum(int(j) * (2 ** i) for i, j in enumerate(inp[::-1]))
  
# Solutin 2
def bin_to_decimal(inp):
    return int(str(inp),2)
