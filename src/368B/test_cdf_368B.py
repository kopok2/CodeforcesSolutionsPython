import unittest
from unittest.mock import patch

from cdf_368B import CodeforcesTask368BSolution


class TestCDF368B(unittest.TestCase):
    def test_368B_acceptance_1(self):
        mock_input = ['10 10', '1 2 3 4 1 2 3 4 100000 99999', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        expected = '6\n6\n6\n6\n6\n5\n4\n3\n2\n1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask368BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
