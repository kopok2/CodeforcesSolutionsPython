import unittest
from unittest.mock import patch

from cdf_75A import CodeforcesTask75ASolution


class TestCDF75A(unittest.TestCase):
    def test_75A_acceptance_1(self):
        mock_input = ['101', '102']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask75ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_75A_acceptance_2(self):
        mock_input = ['105', '106']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask75ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
