# given k linked lists, merge the results in ascending order

from typing import List
from collections import defaultdict
from queue import PriorityQueue

# create a Node object for the Linked List
class ListNode:
    def __init__(self, dataVal) -> None:
        self.dataVal = dataVal
        self.next = None

# SOLUTION: from all front nodes, recurringly add minimum value to resulting list

class Solution:
    def mergeKLists(self, linkedLists: List[ListNode]) -> ListNode:

        result = ListNode(0)
        current = result
        val_to_nodes = defaultdict(list) # O(k)
        pQueue = PriorityQueue() # O(k)
        
        # map each list's first node value to a list of each LinkedList with that initial value
        for node in linkedLists:    # O(k)
            val_to_nodes[node.dataVal].append(node)
            pQueue.put(node.dataVal)

        # loop while there are still nodes left to check in the dict
        while len(val_to_nodes): 
            # find min value using priority queue
            minValue = pQueue.get() # O(log k) as there will only ever be k values in queue

            node = val_to_nodes[minValue].pop() # returns and removes lowest node from map of lists
            current.next = ListNode(node.dataVal)
            current = current.next

            # if the minValue list is not empty, add next node to dict and update queue to have corresponding value
            if node.next:   # O(n) to go through length of longest list
                val_to_nodes[node.next.dataVal].append(node.next)
                pQueue.put(node.next.dataVal)
            
            # if there are no more nodes left corresponding to minValue's list, remove mapping
            if len(val_to_nodes[minValue]) == 0:
                del val_to_nodes[minValue]
            
        return result.next

# Given Test
#List1
list1 = ListNode(1)
list1.next = ListNode(5)
list1.next.next = ListNode(7)
#List2
list2 = ListNode(2)
list2.next = ListNode(3)
list2.next.next = ListNode(6)
list2.next.next.next = ListNode(9)
#List3
list3 = ListNode(4)
list3.next = ListNode(8)
list3.next.next = ListNode(10)

lists = [list1, list2, list3]
sol = Solution()
answer = sol.mergeKLists(lists)
printAns = answer

# Result expected: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> NULL
print("Given test: ", end="")
while printAns:
    if not printAns.next:
        print(printAns.dataVal, end=" -> NULL\n")
    else:
        print(printAns.dataVal, end=" -> ")
    printAns = printAns.next

# Made up test
#List1
list1 = ListNode(1)
list1.next = ListNode(5)
list1.next.next = ListNode(37)
list1.next.next.next = ListNode(79)

#List2
list2 = ListNode(26)
list2.next = ListNode(35)
list2.next.next = ListNode(60)
list2.next.next.next = ListNode(93)
#List3
list3 = ListNode(14)
list3.next = ListNode(80)
list3.next.next = ListNode(100)

lists = [list1, list2, list3]
answer = sol.mergeKLists(lists)
printAns = answer

# Result expected: 1 -> 5 -> 14 -> 26 -> 35 -> 37 -> 60 -> 79 -> 80 -> 93 -> 100 -> NULL
print("Made up test: ", end="")
while printAns:
    if not printAns.next:
        print(printAns.dataVal, end=" -> NULL\n")
    else:
        print(printAns.dataVal, end=" -> ")
    printAns = printAns.next

exit()

'''
OPTIMAL SOLUTION: O(k log k) time complexity, O(n) space
- O(k) to map nodes, O(log k) for PriorityQueue to find min value of k front nodes
- O(n) to store a resulting list with all values from input
'''