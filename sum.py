#Given list of numbers, return sum of those numbers.
    #For example:
    #sum_nums([1, 2, 3, 4])

    #Should return (not print):
    #  10
  
    # Python has a built-in function `sum()` for this, but we don't
    # want you to use it. Please write this by hand.
def sum_nums(nums):
    sum = 0
    for num in nums:
        sum = sum + num
        return sum

#solution question:
print("sum_nums returned", sum_nums([1, 2, 3, 4]))

# Why am I printing if I was told not to and why is it
# even needed after the return?
# Comparing to any7.py which does have a return outside the function,
# Why can't I simply return the function sum_nums instead of 
# the return sum within the function? Or, why can't I do both?
