import unittest
from unittest.mock import patch

from cdf_790A import CodeforcesTask790ASolution


class TestCDF790A(unittest.TestCase):
    def test_790A_acceptance_1(self):
        mock_input = ['8 3', 'NO NO YES YES YES NO']
        expected = 'Adam Bob Bob Cpqepqwer Limak Adam Bob Adam'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask790ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_790A_acceptance_2(self):
        mock_input = ['9 8', 'YES NO']
        expected = 'R Q Ccccccccc Ccocc Ccc So Strong Samples Ccc'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask790ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_790A_acceptance_3(self):
        mock_input = ['3 2', 'NO NO']
        expected = 'Na Na Na'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask790ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
