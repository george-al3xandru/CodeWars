# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

# Note: The function accepts an integer and returns an integer

# Solution 1
def square_digits(num):
    square = ""
    for x in str(num):
        square += str(int(x)**2)
    return int(square)
  
# Solution 2
def square_digits(num):
    square = 0
    i = 1
    while num > 0:
        x = num % 10
        num = num // 10
        square += (x ** 2) * i
        if x <= 3:
            i *= 10
        else:
            i *= 100
    return square
