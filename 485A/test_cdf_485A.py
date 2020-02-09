import unittest
from unittest.mock import patch

from cdf_485A import CodeforcesTask485ASolution


class TestCDF485A(unittest.TestCase):
    def test_485A_acceptance_1(self):
        mock_input = ['1 5']
        expected = 'No'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask485ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_485A_acceptance_2(self):
        mock_input = ['3 6']
        expected = 'Yes'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask485ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
