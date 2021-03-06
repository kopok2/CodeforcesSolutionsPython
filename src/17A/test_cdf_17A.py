import unittest
from unittest.mock import patch

from cdf_17A import CodeforcesTask17ASolution


class TestCDF17A(unittest.TestCase):
    def test_17A_acceptance_1(self):
        mock_input = ['27 2']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask17ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_17A_acceptance_2(self):
        mock_input = ['45 7']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask17ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
