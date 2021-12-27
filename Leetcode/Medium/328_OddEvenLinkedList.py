# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        odd = ListNode()
        odd_head = odd
        even = ListNode()
        even_head = even
        
        current = head
        switch = False # odd=False
        
        while current:
            if switch: # even
                #print("   ",current.val)
                even.next = current
                even = even.next
            else: # odd
                #print(current.val)
                odd.next = current
                odd = odd.next
                
            switch = not switch
            current = current.next
        
        # Remove empty ODD head
        odd_head = odd_head.next
        # Add EVENs to ODD list (remove spacer)
        even.next = None
        odd.next = even_head.next
        
        return odd_head
                
            


"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain as it was in the input.
  You must solve the problem in O(1) extra space complexity and O(n) time complexity.
  
    Input: head = [1,2,3,4,5]
    Output: [1,3,5,2,4]

    Input: head = [2,1,3,5,6,4,7]
    Output: [2,3,6,7,1,5,4]
"""
