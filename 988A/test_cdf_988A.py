import unittest
from unittest.mock import patch

from cdf_988A import CodeforcesTask988ASolution


class TestCDF988A(unittest.TestCase):
    def test_988A_acceptance_1(self):
        mock_input = ['5 3', '15 13 15 15 12']
        expected = 'YES\n1 2 5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask988ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_988A_acceptance_2(self):
        mock_input = ['5 4', '15 13 15 15 12']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask988ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_988A_acceptance_3(self):
        mock_input = ['4 4', '20 10 40 30']
        expected = 'YES\n1 2 3 4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask988ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
