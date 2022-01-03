# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

DEBUG = False

class Solution:
    """Tortoise & Hare cycle-finding algorithm. O(1) space(memory), O(n) time."""
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tortoise = hare = head
        if DEBUG: print(hare.val, "|", tortoise.val)
        # Step 1: Iterate hare(2) and tortoise(1).
        # If there is a cycle, they will meet eventually.
        while hare and hare.next:
            tortoise = tortoise.next # move 1-step at a time
            hare = hare.next.next # move 2-steps at a time
            if DEBUG: print(hare.val, "|", tortoise.val)
            if hare == tortoise:
                if DEBUG: print("-----")
                break
        else: # triggers if while-loop ends from a `break
            return
        if DEBUG: print()
        # Step 2: Reset hare. Move hare & tortoise 1-step at a time each.
        # They WILL [logically] meet at the start of the cycle.
        hare = head
        if DEBUG: print(hare.val, "|", tortoise.val)
        while hare != tortoise:
            # Both are moving 'tortoise-wise' now (1-step):
            hare = hare.next
            tortoise = tortoise.next
            if DEBUG: print(hare.val, "|", tortoise.val)
        return hare



class _Solution:
    """Solution uses a set to check for the Cycle's starting point, 
    but also O(n) memory and O(n) time..."""
    nodes = {}
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return #
        current = head
       
        dupes = set()
        while current not in dupes:
            dupes.add(current)
            try:
                current = current.next
            except:
                return #
        return current
            
        
        

"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
  - There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
  - Do not modify the linked list.

  Example 1:
    Input: head = [3,2,0,-4], pos = 1
    Output: tail connects to node index 1
      Explanation: There is a cycle in the linked list, where tail connects to the second node.
      
  Example 2:
    Input: head = [1,2], pos = 0
    Output: tail connects to node index 0
      Explanation: There is a cycle in the linked list, where tail connects to the first node.
