import unittest
from unittest.mock import patch

from cdf_445B import CodeforcesTask445BSolution


class TestCDF445B(unittest.TestCase):
    def test_445B_acceptance_1(self):
        mock_input = ['1 0']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask445BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_445B_acceptance_2(self):
        mock_input = ['2 1', '1 2']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask445BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_445B_acceptance_3(self):
        mock_input = ['3 2', '1 2', '2 3']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask445BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
