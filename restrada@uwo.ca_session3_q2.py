# Given String s, remove the minimum excess parentheses

# SOLUTION
# loop through every char in input string
# if char is lowercase, add it to result
# if char is opening bracket, add its index to a stack and add to result
# if char is closing bracket and openStack is not empty, add it to result
# if no condition is met, the bracket/char is invalid. Track how many were removed for offset
# Loop thru result string, removing the offset index of all invalid '(' remaining in openStack

class Solution:

    def removeExcessParentheses(self, s: str) -> str:

        openStack = []  # worst case O(n)
        removed = 0
        result = ""

        for char in s:  # O(n)
            if char.islower():
                result += char
            elif char == '(':
                openStack.append(s.index(char)) # O(1)
                result += char
            elif char == ')' and openStack:
                result += char
                openStack.pop()  # O(1)
            else:
                removed += 1
                continue

        # now, remove all excess '('
        while openStack:
            index = openStack.pop() - removed
            result = result[0 : index : ] + result[index + 1 : : ]  # worst case O(n)
        
        return result

sol = Solution()

# Given Test
# expected: "ab(c)d"
s = "a)b(c)d"
print("Given test: " + sol.removeExcessParentheses(s))

# Made up test
# Expected: "(i(d))yes((a)bcd)"
s = "(Hi(d))yes9)((a)bcd))"
print("Made up test: " + sol.removeExcessParentheses(s))

# Expected: "(good)(nfsfe(fd))()"
s = "(good)))(Nnfsfe(fd))()))"
print("Made up test: " + sol.removeExcessParentheses(s))

exit()
'''
OPTIMAL SOLUTION
Time compelxity - O(n) as we loop through entire string
Space complexity - O(n) worst case, if we store every char from input
'''