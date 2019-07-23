import unittest
from unittest.mock import patch

from cdf_220A import CodeforcesTask220ASolution


class TestCDF220A(unittest.TestCase):
    def test_220A_acceptance_1(self):
        mock_input = ['2', '1 2']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask220ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_220A_acceptance_2(self):
        mock_input = ['3', '3 2 1']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask220ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_220A_acceptance_3(self):
        mock_input = ['4', '4 3 2 1']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask220ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
