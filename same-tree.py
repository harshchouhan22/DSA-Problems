
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left  = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
tree_p = TreeNode(1, TreeNode(2), TreeNode(3))
tree_q = TreeNode(1, TreeNode(2), TreeNode(4))

result = Solution().isSameTree(tree_p, tree_q)
print(result)