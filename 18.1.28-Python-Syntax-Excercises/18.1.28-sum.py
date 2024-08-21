# def sum_nums(nums):
#     """Given list of numbers, return sum of those numbers.

#     For example:
#       sum_nums([1, 2, 3, 4])

#     Should return (not print):
#       10
#     """  

#     # Python has a built-in function `sum()` for this, but we don't
#     # want you to use it. Please write this by hand.

#     # YOUR CODE HERE


# print("sum_nums returned", sum_nums([1, 2, 3, 4]))

# v1

"""
Originally I had the total = 0 outside
Moved total = 0 inside, so it is in scope
Created for loop to iterate through the list
  print print(num) was added to debug
  had total += num backwards, so num += total was always 0
  Once flipped to total += num; it worked

"""


def sum_nums(nums):
    total = 0
    for num in nums:
        print(num) # 1
        total += num
    return total
      
print("sum_nums returned", sum_nums([1, 2, 3, 4]))