# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        # Starter = head
        current = head
        # Keep track while walking...:
        prev, nxt = None, None
        
        # Iterate once thru;
        while current:
            #--Remember next item:
            nxt = current.next
            #--Set current.next to last item (reversing):
            current.next = prev # (None at start!)
            #--
            prev = current
            #--Go to next item:
            current = nxt
        return prev
        

        
"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

  Input: head = [1,2,3,4,5]
  Output: [5,4,3,2,1]
  
  Input: head = [1,2]
  Output: [2,1]
"""
