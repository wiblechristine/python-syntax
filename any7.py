# are any of these numbers a 7? true/false
# print one at a time for results of both outcomes,
# comment the other out in the meantime.

def any7(nums):
    for num in nums:
        if num == 7:
            return True

    return False

print("true", any7([0, 3, 7]))
#print("false", any7([4, 9, 11]))

