import unittest
from unittest.mock import patch

from cdf_1097A import CodeforcesTask1097ASolution


class TestCDF1097A(unittest.TestCase):
    def test_1097A_acceptance_1(self):
        mock_input = ['AS 2H 4C TH JH AD']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1097ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1097A_acceptance_2(self):
        mock_input = ['2H 3D 4C AC KD AS']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1097ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1097A_acceptance_3(self):
        mock_input = ['4D AS AC AD AH 5H']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1097ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
