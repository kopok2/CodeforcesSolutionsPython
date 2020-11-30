import unittest
from unittest.mock import patch

from cdf_334A import CodeforcesTask334ASolution


class TestCDF334A(unittest.TestCase):
    def test_334A_acceptance_1(self):
        mock_input = ['2']
        expected = '1 4\n2 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask334ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
