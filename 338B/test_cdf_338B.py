import unittest
from unittest.mock import patch

from cdf_338B import CodeforcesTask338BSolution


class TestCDF338B(unittest.TestCase):
    def test_338B_acceptance_1(self):
        mock_input = ['6 2 3', '1 2', '1 5', '2 3', '3 4', '4 5', '5 6']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask338BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
