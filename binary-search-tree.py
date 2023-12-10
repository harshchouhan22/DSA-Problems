
# Node of tree
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left =None
        self.right = None

def find_LCA(root, node1, node2):
    if root is None or root.value == node1 or root.value == node2:
        return root

    left_LCA = find_LCA(root.left, node1, node2)
    right_LCA = find_LCA(root.right, node1, node2)

    if left_LCA is not None and right_LCA is not None:
        return root

    return left_LCA if left_LCA is not None else right_LCA

root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(30)
root.left.left = TreeNode(5)
root.left.right = TreeNode(15)
root.right.left = TreeNode(25)
root.right.right = TreeNode(35)

result = find_LCA(root, 5, 15)
print("Lowest Common Ancestor: ", result.value if result else "None")




