import unittest
from unittest.mock import patch

from cdf_325A import CodeforcesTask325ASolution


class TestCDF325A(unittest.TestCase):
    def test_325A_acceptance_1(self):
        mock_input = ['5', '0 0 2 3', '0 3 3 5', '2 0 5 2', '3 2 5 5', '2 2 3 3']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask325ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_325A_acceptance_2(self):
        mock_input = ['4', '0 0 2 3', '0 3 3 5', '2 0 5 2', '3 2 5 5']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask325ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
