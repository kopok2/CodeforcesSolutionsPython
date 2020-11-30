import unittest
from unittest.mock import patch

from cdf_767A import CodeforcesTask767ASolution


class TestCDF767A(unittest.TestCase):
    def test_767A_acceptance_1(self):
        mock_input = ['3', '3 1 2']
        expected = '3\n\n2 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask767ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_767A_acceptance_2(self):
        mock_input = ['5', '4 5 1 2 3']
        expected = '5 4\n\n\n3 2 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask767ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
