import unittest
from unittest.mock import patch

from cdf_238A import CodeforcesTask238ASolution


class TestCDF238A(unittest.TestCase):
    def test_238A_acceptance_1(self):
        mock_input = ['3 2']
        expected = '6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask238ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
