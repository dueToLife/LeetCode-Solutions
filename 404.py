# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#get the sum of left tree
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and root.right:
            return self.rightSubTree(root.right)
        elif root.left and not root.right:
            return self.leftSubTree(root.left)
        else:
            return self.leftSubTree(root.left) + self.rightSubTree(root.right)


    def leftSubTree(self, root):
        if not root:
            return 0
        else:
            if not root.left and not root.right:
                return root.val
            elif not root.left and root.right:
                return self.rightSubTree(root.right)
            elif root.left and not root.right:
                return self.leftSubTree(root.left)
            else:
                return self.leftSubTree(root.left) + self.rightSubTree(root.right)

    def rightSubTree(self, root):
        if not root:
            return 0
        else:
            if not root.left and root.right:
                return self.rightSubTree(root.right)
            elif root.left and not root.right:
                return self.leftSubTree(root.left)
            else:
                return self.leftSubTree(root.left) + self.rightSubTree(root.right)