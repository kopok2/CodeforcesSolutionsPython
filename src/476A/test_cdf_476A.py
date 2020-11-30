import unittest
from unittest.mock import patch

from cdf_476A import CodeforcesTask476ASolution


class TestCDF476A(unittest.TestCase):
    def test_476A_acceptance_1(self):
        mock_input = ['10 2']
        expected = '6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask476ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_476A_acceptance_2(self):
        mock_input = ['3 5']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask476ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
