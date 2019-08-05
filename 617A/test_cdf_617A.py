import unittest
from unittest.mock import patch

from cdf_617A import CodeforcesTask617ASolution


class TestCDF617A(unittest.TestCase):
    def test_617A_acceptance_1(self):
        mock_input = ['5']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask617ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_617A_acceptance_2(self):
        mock_input = ['12']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask617ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
