import unittest
from unittest.mock import patch

from cdf_682A import CodeforcesTask682ASolution


class TestCDF682A(unittest.TestCase):
    def test_682A_acceptance_1(self):
        mock_input = ['6 12']
        expected = '14'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask682ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_682A_acceptance_2(self):
        mock_input = ['11 14']
        expected = '31'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask682ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_682A_acceptance_3(self):
        mock_input = ['1 5']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask682ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_682A_acceptance_4(self):
        mock_input = ['3 8']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask682ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_682A_acceptance_5(self):
        mock_input = ['5 7']
        expected = '7'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask682ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_682A_acceptance_6(self):
        mock_input = ['21 21']
        expected = '88'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask682ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
