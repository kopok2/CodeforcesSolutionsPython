import unittest
from unittest.mock import patch

from cdf_893B import CodeforcesTask893BSolution


class TestCDF893B(unittest.TestCase):
    def test_893B_acceptance_1(self):
        mock_input = ['3']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask893BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_893B_acceptance_2(self):
        mock_input = ['992']
        expected = '496'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask893BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
