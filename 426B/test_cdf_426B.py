import unittest
from unittest.mock import patch

from cdf_426B import CodeforcesTask426BSolution


class TestCDF426B(unittest.TestCase):
    def test_426B_acceptance_1(self):
        mock_input = ['4 3', '0 0 1', '1 1 0', '1 1 0', '0 0 1']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask426BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_426B_acceptance_2(self):
        mock_input = ['3 3', '0 0 0', '0 0 0', '0 0 0']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask426BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_426B_acceptance_3(self):
        mock_input = ['8 1', '0', '1', '1', '0', '0', '1', '1', '0']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask426BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
