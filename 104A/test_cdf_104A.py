import unittest
from unittest.mock import patch

from cdf_104A import CodeforcesTask104ASolution


class TestCDF104A(unittest.TestCase):
    def test_104A_acceptance_1(self):
        mock_input = ['12']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask104ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_104A_acceptance_2(self):
        mock_input = ['20']
        expected = '15'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask104ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_104A_acceptance_3(self):
        mock_input = ['10']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask104ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
