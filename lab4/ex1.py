class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None

    def __repr__(self):
        return f"({self.value}, {self.priority})"


class BinaryTreePriorityQueue:
    def __init__(self):
        self.root = None

    def insert(self, value, priority):
        new_node = Node(value, priority)
        if not self.root:
            self.root = new_node
        else:
            self.root = self._insert(self.root, new_node)

    def _insert(self, root, node):
        if node.priority > root.priority:
            node.left = root
            return node
        elif not root.right:
            root.right = node
        else:
            root.right = self._insert(root.right, node)
        return root

    def pop(self):
        if not self.root:
            return None
        max_node = self.root
        self.root = self._merge(self.root.left, self.root.right)
        return max_node

    def _merge(self, left, right):
        if not left:
            return right
        if not right:
            return left

        if left.priority >= right.priority:
            left.right = self._merge(left.right, right)
            return left
        else:
            right.left = self._merge(left, right.left)
            return right

    def peek(self):
        return self.root

    def _traverse(self, node):
        if not node:
            return []
        return [(node.value, node.priority)] + self._traverse(node.left) + self._traverse(node.right)

    def view(self):
        return self._traverse(self.root)

queue = BinaryTreePriorityQueue()
queue.insert("A", 3)
queue.insert("B", 5)
queue.insert("C", 1)
queue.insert("D", 4)

print("Queue view:", queue.view())
print("Peek:", queue.peek())
print("Pop:", queue.pop())
print("Queue view after pop:", queue.view())
