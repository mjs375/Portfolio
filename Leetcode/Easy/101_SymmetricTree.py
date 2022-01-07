# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left, right = root.left, root.right
        return self.help(left,right)
    
    def help(self, left, right):
        """Recursive function. Compares mirrored nodes of a binary tree."""
        # If both null, symmetrical (and no need to recurse further):
        if not left and not right: 
            return True
        
        # If 1/other side is null, asymmetrical:
        if not left or not right:
            return False
        
        # Values don't match?
        if left.val != right.val:
            return False
        
        # Recurse:
        return self.help(left.left, right.right) and self.help(left.right, right.left)
    
    
    
    
    
    
    
    def _isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """Iterative solution. Ugly!"""
        
        if not root:
            return False
        
        stack = [(root.left,root.right)]
        
        while stack:
            
            l, r = stack.pop()
            
            if (l and not r) or (not l and r): #XOR
                return False
            
            # If current node-pairs don't match, kill program:
            if not l and not r:
                continue # skip when both branches end in `None`s
            
            #--Symmetry?
            if l.val != r.val:
                return False
            
            #--Add next stack pairs
            if l.left and r.right:
                stack.append( (l.left, r.right) )
            if l.right and r.left:
                stack.append( (l.right, r.left) )
                
            if l.left and not r.right or l.right and not r.left or r.left and not l.right or r.right and not l.left:
                return False
                
        return True



"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

    1
 2     2 
3 4   4 3
  Input: root = [1,2,2,3,4,4,3]
  Output: true


    1
 2     2
_ 3   _ 3
  Input: root = [1,2,2,null,3,null,3]
  Output: false
"""
