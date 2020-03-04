import unittest
from unittest.mock import patch

from cdf_314B import CodeforcesTask314BSolution


class TestCDF314B(unittest.TestCase):
    def test_314B_acceptance_1(self):
        mock_input = ['10 3', 'abab', 'bab']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask314BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
