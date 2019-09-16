import unittest
from unittest.mock import patch

from cdf_939A import CodeforcesTask939ASolution


class TestCDF939A(unittest.TestCase):
    def test_939A_acceptance_1(self):
        mock_input = ['5', '2 4 5 1 3']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask939ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_939A_acceptance_2(self):
        mock_input = ['5', '5 5 5 5 1']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask939ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
