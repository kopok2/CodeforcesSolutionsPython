import unittest
from unittest.mock import patch

from cdf_1196C import CodeforcesTask1196CSolution


class TestCDF1196C(unittest.TestCase):
    def test_1196C_acceptance_1(self):
        mock_input = ['4 2 -1 -2 0 0 0 0 -1 -2 0 0 0 0 3 1 5 1 1 1 1 2 5 0 1 0 1 3 5 1 0 0 0 2 1337 1337 0 1 1 1 1336 1337 1 1 0 1 1 3 5 1 1 1 1']
        expected = '1 -1 -2 1 2 5 0 1 -100000 -100000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1196CSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
