import unittest
from unittest.mock import patch

from cdf_1107B import CodeforcesTask1107BSolution


class TestCDF1107B(unittest.TestCase):
    def test_1107B_acceptance_1(self):
        mock_input = ['3 1 5 5 2 3 1']
        expected = '5 38 19'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1107BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
