import unittest
import os
from src.best_career import best_career

class TestBestCareer(unittest.TestCase):
    def test_example_case(self):
        input_data = "4\n4\n3 1\n2 1 5\n1 3 2 1\n"
        expected_output = "12\n"

        input_filename = "test_input.in"
        output_filename = "test_output.out"

        with open(input_filename, 'w') as f:
            f.write(input_data)

        best_career(input_filename, output_filename)

        with open(output_filename) as f:
            result = f.read()

        self.assertEqual(result, expected_output)

        os.remove(input_filename)
        os.remove(output_filename)

if __name__ == '__main__':
    unittest.main()

