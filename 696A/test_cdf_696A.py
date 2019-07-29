import unittest
from unittest.mock import patch

from cdf_696A import CodeforcesTask696ASolution


class TestCDF696A(unittest.TestCase):
    def test_696A_acceptance_1(self):
        mock_input = ['7', '1 3 4 30', '1 4 1 2', '1 3 6 8', '2 4 3', '1 6 1 40', '2 3 7', '2 2 4']
        expected = '94\n0\n32'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask696ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
