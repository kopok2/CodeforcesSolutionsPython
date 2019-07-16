import unittest
from unittest.mock import patch

from cdf_304A import CodeforcesTask304ASolution


class TestCDF304A(unittest.TestCase):
    def test_304A_acceptance_1(self):
        mock_input = ['5']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask304ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_304A_acceptance_2(self):
        mock_input = ['74']
        expected = '35'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask304ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
