import unittest
from unittest.mock import patch

from cdf_544A import CodeforcesTask544ASolution


class TestCDF544A(unittest.TestCase):
    def test_544A_acceptance_1(self):
        mock_input = ['1', 'abca']
        expected = 'YES\nabca'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask544ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_544A_acceptance_2(self):
        mock_input = ['2', 'aaacas']
        expected = 'YES\naaa\ncas'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask544ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_544A_acceptance_3(self):
        mock_input = ['4', 'abc']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask544ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
