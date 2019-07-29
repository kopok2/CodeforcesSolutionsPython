import unittest
from unittest.mock import patch

from cdf_1101B import CodeforcesTask1101BSolution


class TestCDF1101B(unittest.TestCase):
    def test_1101B_acceptance_1(self):
        mock_input = ['|[a:b:|]']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1101BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1101B_acceptance_2(self):
        mock_input = ['|]:[|:]']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1101BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
