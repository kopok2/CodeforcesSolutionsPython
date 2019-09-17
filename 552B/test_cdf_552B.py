import unittest
from unittest.mock import patch

from cdf_552B import CodeforcesTask552BSolution


class TestCDF552B(unittest.TestCase):
    def test_552B_acceptance_1(self):
        mock_input = ['13']
        expected = '17'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask552BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_552B_acceptance_2(self):
        mock_input = ['4']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask552BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
