import unittest
from unittest.mock import patch

from cdf_591A import CodeforcesTask591ASolution


class TestCDF591A(unittest.TestCase):
    def test_591A_acceptance_1(self):
        mock_input = ['100', '50', '50']
        expected = '50'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask591ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_591A_acceptance_2(self):
        mock_input = ['199', '60', '40']
        expected = '119.4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask591ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
