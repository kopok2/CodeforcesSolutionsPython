import unittest
from unittest.mock import patch

from cdf_411A import CodeforcesTask411ASolution


class TestCDF411A(unittest.TestCase):
    def test_411A_acceptance_1(self):
        mock_input = ['abacaba']
        expected = 'Too weak'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask411ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_411A_acceptance_2(self):
        mock_input = ['X12345']
        expected = 'Too weak'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask411ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_411A_acceptance_3(self):
        mock_input = ['CONTEST_is_STARTED!!11']
        expected = 'Correct'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask411ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
