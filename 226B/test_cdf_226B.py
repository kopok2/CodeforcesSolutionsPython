import unittest
from unittest.mock import patch

from cdf_226B import CodeforcesTask226BSolution


class TestCDF226B(unittest.TestCase):
    def test_226B_acceptance_1(self):
        mock_input = ['5', '2 3 4 1 1', '2', '2 3']
        expected = '9 8'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask226BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
