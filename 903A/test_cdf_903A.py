import unittest
from unittest.mock import patch

from cdf_903A import CodeforcesTask903ASolution


class TestCDF903A(unittest.TestCase):
    def test_903A_acceptance_1(self):
        mock_input = ['2', '6', '5']
        expected = 'YES\nNO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask903ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
