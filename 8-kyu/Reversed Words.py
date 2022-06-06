# Complete the solution so that it reverses all of the words within the string passed in.

# Example(Input --> Output):
# "The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"

def reverse_words(s):
    words = s.split()
    return " ".join(i for i in words[::-1])
