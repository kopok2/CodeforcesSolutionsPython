import unittest
from unittest.mock import patch

from cdf_710B import CodeforcesTask710BSolution


class TestCDF710B(unittest.TestCase):
    def test_710B_acceptance_1(self):
        mock_input = ['4', '1 2 3 4']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask710BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
