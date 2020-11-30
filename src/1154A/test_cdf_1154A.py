import unittest
from unittest.mock import patch

from cdf_1154A import CodeforcesTask1154ASolution


class TestCDF1154A(unittest.TestCase):
    def test_1154A_acceptance_1(self):
        mock_input = ['3 6 5 4']
        expected = '2 1 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1154ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1154A_acceptance_2(self):
        mock_input = ['40 40 40 60']
        expected = '20 20 20'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1154ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1154A_acceptance_3(self):
        mock_input = ['201 101 101 200']
        expected = '1 100 100'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1154ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
