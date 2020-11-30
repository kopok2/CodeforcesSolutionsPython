import unittest
from unittest.mock import patch

from cdf_542A import CodeforcesTask542ASolution


class TestCDF542A(unittest.TestCase):
    def test_542A_acceptance_1(self):
        mock_input = ['2 3', '7 9', '1 4', '2 8 2', '0 4 1', '8 9 3']
        expected = '4\n2 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask542ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_542A_acceptance_2(self):
        mock_input = ['1 1', '0 0', '1 1 10']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask542ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
