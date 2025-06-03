import unittest
from ex import TreeNode, sum_of_depths

class TestSumOfDepths(unittest.TestCase):
    def test_example_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertEqual(sum_of_depths(root), 6)

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(sum_of_depths(root), 0)

    def test_empty_tree(self):
        self.assertEqual(sum_of_depths(None), 0)

    def test_deeper_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        self.assertEqual(sum_of_depths(root), 6)

if __name__ == "__main__":
    unittest.main()
