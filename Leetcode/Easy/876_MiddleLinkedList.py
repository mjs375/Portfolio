# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Traverse list with a pointer, slow.
        Simultaneously, traverse with a pointer (twice as)'fast'.
        When fast reaches the end, slow must be in the middle.
        """
        
        slow = fast = head
        
        while fast and fast.next:
            print(slow.val, fast.val)
            slow = slow.next        # 1 2 3 4 5* ...
            fast = fast.next.next   # 1 3 5 7 9 ...
        return slow
        
"""
Original plan was to  travel list through once, reversing list as we go,
so that at the end, my counter would tell me how many steps to trace back to
know half the length. Unfortunately, this also returns the opposite half of the 
linked-list since it was reversed, and requires running through the list 1.5 times.
"""


"""
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example 1:
  Input: head = [1,2,3,4,5]
  Output: [3,4,5]
   Explanation: The middle node of the list is node 3.
   
Example 2:
  Input: head = [1,2,3,4,5,6]
  Output: [4,5,6]
    Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
"""
