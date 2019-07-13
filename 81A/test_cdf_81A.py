import unittest
from unittest.mock import patch

from cdf_81A import CodeforcesTask81ASolution


class TestCDF81A(unittest.TestCase):
    def test_81A_acceptance_1(self):
        mock_input = ['hhoowaaaareyyoouu']
        expected = 'wre'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask81ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_81A_acceptance_2(self):
        mock_input = ['reallazy']
        expected = 'rezy'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask81ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_81A_acceptance_3(self):
        mock_input = ['abacabaabacabaa']
        expected = 'a'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask81ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
