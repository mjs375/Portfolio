# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # Container for all nodes
        self.nodes = []
        
        # Iterate each list
        for l in lists:
            # Exhaust each list til end
            while l:
                # Add every node to container
                self.nodes.append(l.val)
                # Go to next node
                l = l.next
        
        # 
        head = ListNode(0)
        pointer = head
        # Iterate all values
        for value in sorted(self.nodes):
            # Add value as node to end of linked list
            pointer.next = ListNode(value)
            # Point pointer to next item
            pointer = pointer.next
            
        return head.next


"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

 
Example 1:
  Input: lists = [[1,4,5],[1,3,4],[2,6]]
  Output: [1,1,2,3,4,4,5,6]
    Explanation: The linked-lists are:
    [
      1->4->5,
      1->3->4,
      2->6
    ]
    Merging them into one sorted list:
      1->1->2->3->4->4->5->6

Example 2:
  Input: lists = []
  Output: []
Example 3:
  Input: lists = [[]]
  Output: []
"""
