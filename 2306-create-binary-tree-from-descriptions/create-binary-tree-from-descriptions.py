# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes,childs = defaultdict(lambda:[0,0]), set()
        for d in descriptions:  nodes[d[0]][1-d[2]] = d[1]; childs.add(d[1])
        def tree(val): return None if not val else TreeNode(val, tree(nodes[val][0]), tree(nodes[val][1]))
        return tree((set(nodes.keys()) - childs).pop())
        