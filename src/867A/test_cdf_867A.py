import unittest
from unittest.mock import patch

from cdf_867A import CodeforcesTask867ASolution


class TestCDF867A(unittest.TestCase):
    def test_867A_acceptance_1(self):
        mock_input = ['4', 'FSSF']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask867ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_867A_acceptance_2(self):
        mock_input = ['2', 'SF']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask867ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_867A_acceptance_3(self):
        mock_input = ['10', 'FFFFFFFFFF']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask867ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_867A_acceptance_4(self):
        mock_input = ['10', 'SSFFSFFSFF']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask867ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
