import unittest
from unittest.mock import patch

from cdf_805B import CodeforcesTask805BSolution


class TestCDF805B(unittest.TestCase):
    def test_805B_acceptance_1(self):
        mock_input = ['2']
        expected = 'aa'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask805BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_805B_acceptance_2(self):
        mock_input = ['3']
        expected = 'bba'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask805BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
