# DESCRIPTION:
# You're writing code to control your town's traffic lights. You need a function to handle each change from green, to yellow, to red, and then to green again.

# Complete the function that takes a string as an argument representing the current state of the light and returns a string representing the state the light
# should change to.

# For example, when the input is green, output should be yellow.

# Solution 1
def update_light(current):
    lights = ["green", "yellow", "red"]
    for i, n in enumerate(lights):
        if n == current:
            return lights[0] if i == len(lights) - 1 else lights[i + 1]
        
# Solution 2
def update_light(current):
    lights = {
        "green" : "yellow",
        "yellow": "red"   ,
        "red"   : "green" 
    }
    return lights[current] if current in lights.keys() else "Invalid Colour"
