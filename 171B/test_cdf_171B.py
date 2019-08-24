import unittest
from unittest.mock import patch

from cdf_171B import CodeforcesTask171BSolution


class TestCDF171B(unittest.TestCase):
    def test_171B_acceptance_1(self):
        mock_input = ['2']
        expected = '13'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask171BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
