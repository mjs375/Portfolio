# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self,p,q):
        """Using DFS/stack algorithm. 
        Remember, a Python list is a Stack using .pop()!"""
        print()

        stack = [ (p,q) ] # DFS Stack
        
        while stack:
            
            #--Grab a pair of nodes (e.g. `1|1`)
            p, q = stack.pop() # last-in, first-out (DFS)
 
            if (p and not q) or (not p and q): #XOR
                return False
            
            # If current node-pairs don't match, kill program:
            if not p and not q:
                continue # skip when both branches end in `None`s
                
            if p.val != q.val:
                return False # if mismatched pair, FAIL!

            stack.extend( [(p.left, q.left), (p.right, q.right)] )
            
        return True
            
    def _isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pass    
      
"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
  Input: p = [1,2,3], q = [1,2,3]
    Output: true
    
Example 2:
  Input: p = [1,2], q = [1,null,2]
    Output: false
    
Example 3:
  Input: p = [1,2,1], q = [1,1,2]
    Output: false
"""
