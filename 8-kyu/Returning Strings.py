# Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".
# [Make sure you type the exact thing I wrote or the program may not execute properly]

# Solution 1:
def greet(name):
    return f'Hello, {name} how are you doing today?'
  
# Solution 2:
def greet(name):
    return "Hello, {} how are you doing today?".format(name)
