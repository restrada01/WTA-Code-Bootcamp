# find if a subarray exists whose sum equals to 0

# if we track the sum of all numbers while traversing the array, a sum can only reoccur if there exists a subarray which sums to zero
# use a set to track unique sums, and if the current sum ever repeats the problem is solved

def tempSubarraySum(array):

    # variables for looping through array and storing past sums
    length = len(array)
    sum = 0
    prevSum_Set = set()

    for i in range(length):
        sum += array[i]
        # if sum is zero, problem is solved
        # if sum has been saved before, a subarray exists which satisfies conditions
        if sum == 0 or sum in prevSum_Set:
            return True
        prevSum_Set.add(sum)
    # return False if there is no zero or existing sum found
    return False        

# Time complexity: O(n) since one for loop
# Space: O(n) since using set but better to sacrifice space over time

# Given tests
input = [4, 2, -3, 1, 6]
print(tempSubarraySum(input))
input = [4, 2, 0, 1, 6]
print(tempSubarraySum(input))
input = [-3, 2, 3, 1, 6]
print(tempSubarraySum(input))

## Made up tests
input = [8, 9, -5, -7, 3]   # should be True
print(tempSubarraySum(input))

input = [1, 1, 5, -4, -7]   # shound be False
print(tempSubarraySum(input))

exit()
