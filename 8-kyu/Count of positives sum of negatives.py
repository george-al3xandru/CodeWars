# Given an array of integers.
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.
# If the input is an empty array or is null, return an empty array.

# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

# Solution 1
def count_positives_sum_negatives(arr):
    new_arr = []
    if arr:
        negative = 0
        positive_count = 0
        for i in arr:
            if i <= 0:
                negative += i
            else:
                positive_count += 1
        new_arr.append(positive_count)
        new_arr.append(negative)
    return new_arr
  
# Solution 2
def count_positives_sum_negatives(arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []
