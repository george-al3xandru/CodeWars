# Write a function that returns a string in which firstname is swapped with last name.

def name_shuffler(str):
    reverse_str = ""
    pos = 0
    x = str.split(" ")
    for i in x[::-1]:
        pos += 1
        if pos == len(x):
            reverse_str += i
        else:
            reverse_str += i + " "
    return reverse_str
