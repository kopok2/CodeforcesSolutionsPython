import unittest
from unittest.mock import patch

from cdf_120C import CodeforcesTask120CSolution


class TestCDF120C(unittest.TestCase):
    def test_120C_acceptance_1(self):
        mock_input = ['3 3', '15 8 10']
        expected = '9'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask120CSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
