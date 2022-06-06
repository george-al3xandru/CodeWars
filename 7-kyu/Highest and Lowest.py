# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

# Examples
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"
# Notes
# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number is first.

# Solution 1
def high_and_low(numbers):
    num = numbers.split(" ")
    min = num[0]
    max = num[0]
    for i in num:
        if int(i) < int(min):
            min = i
        if int(i) > int(max):
            max = i
    return f"{max} {min}"
 
# Solution 2
def high_and_low(numbers):
  nums = sorted(numbers.split(), key=int)
  return '{} {}'.format(nums[-1], nums[0])
