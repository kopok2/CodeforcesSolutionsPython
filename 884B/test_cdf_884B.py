import unittest
from unittest.mock import patch

from cdf_884B import CodeforcesTask884BSolution


class TestCDF884B(unittest.TestCase):
    def test_884B_acceptance_1(self):
        mock_input = ['2 4', '1 3']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask884BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_884B_acceptance_2(self):
        mock_input = ['3 10', '3 3 2']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask884BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_884B_acceptance_3(self):
        mock_input = ['2 10', '1 3']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask884BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
