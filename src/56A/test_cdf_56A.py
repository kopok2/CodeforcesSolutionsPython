import unittest
from unittest.mock import patch

from cdf_56A import CodeforcesTask56ASolution


class TestCDF56A(unittest.TestCase):
    def test_56A_acceptance_1(self):
        mock_input = ['5', '18', 'VODKA', 'COKE', '19', '17']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask56ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
