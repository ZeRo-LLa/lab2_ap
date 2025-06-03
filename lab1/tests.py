import unittest
from ex import is_monotonic 

class TestMonotonicArray(unittest.TestCase):
    def test_increasing(self):
        self.assertTrue(is_monotonic([1, 2, 3, 4, 5])[0])  
    
    def test_decreasing(self):
        self.assertTrue(is_monotonic([5, 4, 3, 2, 1])[0])
    
    def test_non_monotonic(self):
        self.assertFalse(is_monotonic([1, 2, 2, 3, 2, 4])[0]) 
    
    def test_constant(self):
        self.assertTrue(is_monotonic([3, 3, 3, 3])[0])
    
    def test_single_element(self):
        self.assertTrue(is_monotonic([10])[0])
    
    def test_empty_array(self):
        self.assertTrue(is_monotonic([])[0])


unittest.main()
