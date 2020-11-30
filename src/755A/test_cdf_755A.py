import unittest
from unittest.mock import patch

from cdf_755A import CodeforcesTask755ASolution


class TestCDF755A(unittest.TestCase):
    def test_755A_acceptance_1(self):
        mock_input = ['3']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask755ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_755A_acceptance_2(self):
        mock_input = ['4']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask755ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
