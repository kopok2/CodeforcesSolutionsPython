import unittest
from unittest.mock import patch

from cdf_977A import CodeforcesTask977ASolution


class TestCDF977A(unittest.TestCase):
    def test_977A_acceptance_1(self):
        mock_input = ['512 4']
        expected = '50'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask977ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_977A_acceptance_2(self):
        mock_input = ['1000000000 9']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask977ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
