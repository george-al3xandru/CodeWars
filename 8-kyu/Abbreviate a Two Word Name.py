# Task
# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

# The output should be two capital letters with a dot separating them.

# It should look like this:
# Sam Harris => S.H
# patrick feeney => P.F

# Solution 1
def abbrev_name(name):
    initials = name[0] + "."
    for i, n in enumerate(name):
        if n == " ":
            initials += name[i+1]
    return initials.upper()
 
# Solution 2
 def abbrev_name(name):
    return '.'.join(i[0] for i in name.split()).upper()
