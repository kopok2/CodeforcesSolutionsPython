import unittest
from unittest.mock import patch

from cdf_569A import CodeforcesTask569ASolution


class TestCDF569A(unittest.TestCase):
    def test_569A_acceptance_1(self):
        mock_input = ['5 2 2']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask569ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_569A_acceptance_2(self):
        mock_input = ['5 4 7']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask569ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_569A_acceptance_3(self):
        mock_input = ['6 2 3']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask569ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
