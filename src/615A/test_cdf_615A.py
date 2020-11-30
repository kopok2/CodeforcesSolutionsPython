import unittest
from unittest.mock import patch

from cdf_615A import CodeforcesTask615ASolution


class TestCDF615A(unittest.TestCase):
    def test_615A_acceptance_1(self):
        mock_input = ['3 4', '2 1 4', '3 1 3 1', '1 2']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask615ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_615A_acceptance_2(self):
        mock_input = ['3 3', '1 1', '1 2', '1 1']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask615ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
