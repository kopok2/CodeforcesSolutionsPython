import unittest
from unittest.mock import patch

from cdf_38A import CodeforcesTask38ASolution


class TestCDF38A(unittest.TestCase):
    def test_38A_acceptance_1(self):
        mock_input = ['3', '5 6', '1 2']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask38ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_38A_acceptance_2(self):
        mock_input = ['3', '5 6', '1 3']
        expected = '11'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask38ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
