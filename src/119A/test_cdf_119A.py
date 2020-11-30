import unittest
from unittest.mock import patch

from cdf_119A import CodeforcesTask119ASolution


class TestCDF119A(unittest.TestCase):
    def test_119A_acceptance_1(self):
        mock_input = ['3 5 9']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask119ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_119A_acceptance_2(self):
        mock_input = ['1 1 100']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask119ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
