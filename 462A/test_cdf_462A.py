import unittest
from unittest.mock import patch

from cdf_462A import CodeforcesTask462ASolution


class TestCDF462A(unittest.TestCase):
    def test_462A_acceptance_1(self):
        mock_input = ['3', 'xxo', 'xox', 'oxx']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask462ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_462A_acceptance_2(self):
        mock_input = ['4', 'xxxo', 'xoxo', 'oxox', 'xxxx']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask462ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
