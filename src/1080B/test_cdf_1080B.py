import unittest
from unittest.mock import patch

from cdf_1080B import CodeforcesTask1080BSolution


class TestCDF1080B(unittest.TestCase):
    def test_1080B_acceptance_1(self):
        mock_input = ['5 1 3 2 5 5 5 4 4 2 3']
        expected = '-2 -2 -5 4 -1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1080BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
