import unittest
from ex import min_time_to_paint

def user_input():
    K, T, *L = map(int, input("Введіть K, T та довжини щитів через пробіл: ").split())
    return K, T, L

class TestPainterPartition(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(min_time_to_paint(10, 5, [10, 15, 10, 5, 10, 15, 20, 20, 15, 20]), 100)
    
    def test_single_painter(self):
        self.assertEqual(min_time_to_paint(1, 2, [5, 10, 15]), 60)
    
    def test_equal_painters_boards(self):
        self.assertEqual(min_time_to_paint(3, 1, [10, 20, 30]), 30)
    
    def test_more_painters_than_boards(self):
        self.assertEqual(min_time_to_paint(5, 3, [2, 4, 6, 8]), 24)

if __name__ == "__main__":
    K, T, L = user_input()
    print(min_time_to_paint(K, T, L))
    unittest.main()
