import unittest
from unittest.mock import patch

from cdf_862B import CodeforcesTask862BSolution


class TestCDF862B(unittest.TestCase):
    def test_862B_acceptance_1(self):
        mock_input = ['3', '1 2', '1 3']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask862BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_862B_acceptance_2(self):
        mock_input = ['5', '1 2', '2 3', '3 4', '4 5']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask862BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
