# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        new = ListNode() # 'empty' 1st node to start
        new.next = head # set the 2nd node as head
        current = new # start the iterator at the empty elem (in case '1st' node is `val`)
        
        #--Iterate: look ahead at next Node:
        while current.next:
            #--If next Node is target, link current node to next-next node, overwriting it
            if current.next.val == val:
                current.next = current.next.next
            #--else, traverse as usual
            else:
                current = current.next
                
        # Skip the 'empty' 1st node:
        new = new.next
        return new



"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Input: head = [], val = 1
Output: []

Input: head = [7,7,7,7], val = 7
Output: []
"""
