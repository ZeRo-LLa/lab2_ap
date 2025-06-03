import unittest
from src.root_vertex import is_root_vertex

class TestRootVertex(unittest.TestCase):
    def test_example(self):
        graph = [
            [1],
            [2],
            [3],
            [0],
            [3],
            [0]
        ]
        self.assertTrue(is_root_vertex(graph, 5)) 

if __name__ == "__main__":
    unittest.main()
