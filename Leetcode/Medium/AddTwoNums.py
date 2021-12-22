# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:        
    def addTwoNumbers(self, l1, l2, carryover=0) -> Optional[ListNode]:
        """Recursive.
        carryover: val (if >10)."""
        #
        summ = l1.val + l2.val + carryover
        carryover = summ // 10 # remainder if > 10
        l3 = ListNode(summ % 10) # really, l3
        
        #--If anything is still leftover (ListNodes not the same len)
        if l1.next or l2.next or carryover:
            if not l1.next:
                l1.next = ListNode(0) # just make a 0
            if not l2.next:
                l2.next = ListNode(0)
            # Recurse: next l1/l2, pass along remainder
            l3.next = self.addTwoNumbers(l1.next,l2.next,carryover)
        return l3

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
  Example 1:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
      Explanation: 342 + 465 = 807.

"""
