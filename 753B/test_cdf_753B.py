import unittest
from unittest.mock import patch

from cdf_753B import CodeforcesTask753BSolution


class TestCDF753B(unittest.TestCase):
    def test_753B_acceptance_1(self):
        mock_input = ['0 1', '2 0', '1 1', '0 4', '2 1', '4 0']
        expected = '8000\n0179\n3159\n3210\n0112\n0123'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask753BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
