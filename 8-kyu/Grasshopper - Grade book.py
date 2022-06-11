# Grade book
# Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

# Numerical Score	          Letter Grade
# 90 <= score <= 100	          'A'
# 80 <= score < 90	            'B'
# 70 <= score < 80	            'C'
# 60 <= score < 70	            'D'
# 0 <= score < 60	              'F'
# Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.

# Solution 1
def get_grade(s1, s2, s3):
    average = (s1 + s2 + s3) / 3
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
      
 # Solution 2
def get_grade(s1, s2, s3):
    average = (s1 + s2 + s3) / 3
    for score, grade in [(90, 'A'), (80, 'B'), (70, 'C'), (60, 'D'), (0, 'F')]:
        if average >= score:
            return grade

# Solution 3
scores = {10: 'A', 9: 'A', 8: 'B', 7: 'C', 6: 'D'}
def get_grade(*args):
    average = sum(args) / len(args)
    return scores.get(average // 10, 'F') 

# *args The asterisk is used incase any number of amount of values are passed into the function so it is not just limited to three as given in the problem description.
