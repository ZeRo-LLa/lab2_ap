import unittest
from ex1 import BinaryTreePriorityQueue


class TestBinaryTreePriorityQueue(unittest.TestCase):

    def setUp(self):
        self.queue = BinaryTreePriorityQueue()

    def test_insert_and_peek(self):
        self.queue.insert("Task A", 3)
        self.queue.insert("Task B", 5)
        self.queue.insert("Task C", 1)
        self.queue.insert("Task D", 4)

        peeked = self.queue.peek()
        self.assertEqual(peeked.value, "Task B")
        self.assertEqual(peeked.priority, 5)

    def test_pop(self):
        self.queue.insert("Task A", 3)
        self.queue.insert("Task B", 5)
        self.queue.insert("Task C", 2)

        popped = self.queue.pop()
        self.assertEqual(popped.value, "Task B")
        self.assertEqual(popped.priority, 5)

        new_peek = self.queue.peek()
        self.assertEqual(new_peek.value, "Task A")

    def test_view(self):
        self.queue.insert("A", 1)
        self.queue.insert("B", 2)
        self.queue.insert("C", 3)

        view = self.queue.view()
        values = [val for val, _ in view]
        priorities = [priority for _, priority in view]

        self.assertIn("C", values)
        self.assertIn("B", values)
        self.assertIn("A", values)
        self.assertIn(3, priorities)
        self.assertIn(2, priorities)
        self.assertIn(1, priorities)

    def test_empty_queue(self):
        self.assertIsNone(self.queue.peek())
        self.assertIsNone(self.queue.pop())
        self.assertEqual(self.queue.view(), [])


if __name__ == '__main__':
    unittest.main()
