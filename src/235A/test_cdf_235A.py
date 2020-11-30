import unittest
from unittest.mock import patch

from cdf_235A import CodeforcesTask235ASolution


class TestCDF235A(unittest.TestCase):
    def test_235A_acceptance_1(self):
        mock_input = ['9']
        expected = '504'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask235ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_235A_acceptance_2(self):
        mock_input = ['7']
        expected = '210'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask235ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
