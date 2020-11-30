import unittest
from unittest.mock import patch

from cdf_1186A import CodeforcesTask1186ASolution


class TestCDF1186A(unittest.TestCase):
    def test_1186A_acceptance_1(self):
        mock_input = ['5 8 6']
        expected = 'Yes'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1186ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1186A_acceptance_2(self):
        mock_input = ['3 9 3']
        expected = 'Yes'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1186ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1186A_acceptance_3(self):
        mock_input = ['8 5 20']
        expected = 'No'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1186ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
