# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # initialize as -inf then optimize for best
        self.best = float("-inf")
        def DFS(node):
            """
            Depth First Search
            """
            if node is None:
                ''' recursive collapse condition:
                if this doesnt exist return '''
                return 0
            # gains by going left apply DFS
            leftGain = max(DFS(node.left), 0)
            # gains by going right apply DFS
            rightGain = max(DFS(node.right), 0)
            # if elbow of a path max
            self. best = max(self.best, node.val + leftGain + rightGain)
            return node.val + max(leftGain, rightGain)
        # do DFS
        DFS(root)
        return self.best
        