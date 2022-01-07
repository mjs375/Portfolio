# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isUnivalTree(self, root):
        
        def traverse(side,univalue):
            """Helper function to traverse an entire Tree."""
            
            return side == None or ( # return True if at bottom (.val is None)    --OR--
                side.val == univalue and  # is node.val == target?
                traverse(side.left, univalue) and  # AND...
                traverse(side.right, univalue)  # AND...
                ) # AND... complete for all nodes until side==None or side.val!=target
    
        univalue = root.val
        #--Recurse down all nodes of tree:
        return traverse(root.left,univalue) and traverse(root.right, univalue)
        
"""
A binary tree is uni-valued if every node in the tree has the same value.
Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

Example 1:
  Input: root = [1,1,1,1,1,null,1]
  Output: true
Example 2:
  Input: root = [2,2,2,5,2]
  Output: false

"""
