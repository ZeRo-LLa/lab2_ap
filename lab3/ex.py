class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def sum_of_depths(root: TreeNode) -> int:
    if root is None:
        return 0

    stack = [(root, 0)]
    total_depth = 0

    while stack:
        node, depth = stack.pop()
        total_depth += depth 

        if node.right:
            stack.append((node.right, depth + 1))
        if node.left:
            stack.append((node.left, depth + 1))

    return total_depth

root = TreeNode(1, 
                TreeNode(2, 
                         TreeNode(4),
                         None),
                TreeNode(3,
                         None,
                         TreeNode(5)) 
               )

print("Сума глибин для root:", sum_of_depths(root))
