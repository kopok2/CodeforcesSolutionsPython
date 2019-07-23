import unittest
from unittest.mock import patch

from cdf_484A import CodeforcesTask484ASolution


class TestCDF484A(unittest.TestCase):
    def test_484A_acceptance_1(self):
        mock_input = ['3', '1 2', '2 4', '1 10']
        expected = '1\n3\n7'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask484ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
