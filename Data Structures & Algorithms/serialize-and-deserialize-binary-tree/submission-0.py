# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # we input values here to serialize
        values = []
        def DFS(node):
            """
            use depth first search to convert tree to serialized form
            """
            if node is None:
                ''' replace nulls with '#' 
                return becuse nothing is further down and collapse the recrsion
                '''
                values.append("#")
                return
            # send value of current node to values
            values.append(str(node.val))
            # DFS; recurse left
            DFS(node.left)
            # DFS; recurse right
            DFS(node.right)
        # encode using Depth first search
        DFS(root)
        return ",".join(values)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = data.split(",")
        index = [0]  # A list lets the nested function update the index.

        def DFS():
            """
             use a sort of depth first search to convert serialized string to tree
            """
            # line value to curr node
            value = values[index[0]]
            # update for every time this is called
            index[0] += 1
            if value == "#":
                ''' collapse recursion for this branch if hitting a null '''
                return None
            # make a tree node for curr val
            node = TreeNode(int(value))
            # recurse to the left side
            node.left = DFS()
            # recurse to the right side
            node.right = DFS()
            # return (sub)tree
            return node
        # do deserialization using DFS
        return DFS()
