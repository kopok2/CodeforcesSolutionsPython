import unittest
from unittest.mock import patch

from cdf_1076A import CodeforcesTask1076ASolution


class TestCDF1076A(unittest.TestCase):
    def test_1076A_acceptance_1(self):
        mock_input = ['3 aaa']
        expected = 'aa'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1076ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_1076A_acceptance_2(self):
        mock_input = ['5 abcda']
        expected = 'abca'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1076ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
