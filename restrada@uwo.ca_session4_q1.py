# Given the root of a binary tree, return
# the values of the nodes you can see from top to bottom on the right

'''
SOLUTION
- Check that there is a root with a tree to traverse
- starting at level 0, append all nodes into a queue
- add each node's children into the queue to navigate the next level (O(n) as you go through every node)
- if the node being traversed is the last index for that level then add to result
'''

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rhsOrderedList(self, root:TreeNode) -> List[int]:
        # validate input
        if not root:
            return []
        
        q = [root] # Worst case O(n) space complexity
        res = []
        while q:    # O(n) time complexity to traverse through every node in the tree
            n = len(q)
            for node in range(n):
                popped = q.pop(0)
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
                if node == n - 1:      # if the node is the last index in the queue, it is the RHS node
                    res.append(popped.val) 

        return res


#  Given Test

#        1
#       / \
#      2   3
#       \   \
#        5   4

root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.right = TreeNode(4)

sol = Solution()
print(sol.rhsOrderedList(root)) # expected [1, 3, 4]

# Made up test

#        1
#       / \
#      2   4
#       \   \
#        5   6
#       /   / 
#      7   6  
#     /     \
#     9       10

root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(7)
root.left.right.left.left = TreeNode(9)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(6)
root.right.right.left.right = TreeNode(10)


print(sol.rhsOrderedList(root)) # expected [1, 4, 6, 6, 10]


'''
Time complexity: O(n) as we traverse the entire tree
Space Complexity: O(n) 
'''