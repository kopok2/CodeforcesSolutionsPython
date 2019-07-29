import unittest
from unittest.mock import patch

from cdf_890A import CodeforcesTask890ASolution


class TestCDF890A(unittest.TestCase):
    def test_890A_acceptance_1(self):
        mock_input = ['1 3 2 1 2 1']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask890ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_890A_acceptance_2(self):
        mock_input = ['1 1 1 1 1 99']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask890ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
