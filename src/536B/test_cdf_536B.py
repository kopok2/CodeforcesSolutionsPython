import unittest
from unittest.mock import patch

from cdf_536B import CodeforcesTask536BSolution


class TestCDF536B(unittest.TestCase):
    def test_536B_acceptance_1(self):
        mock_input = ['6 2', 'ioi', '1 3']
        expected = '26'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask536BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_536B_acceptance_2(self):
        mock_input = ['5 2', 'ioi', '1 2']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask536BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
