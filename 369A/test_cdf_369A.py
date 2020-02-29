import unittest
from unittest.mock import patch

from cdf_369A import CodeforcesTask369ASolution


class TestCDF369A(unittest.TestCase):
    def test_369A_acceptance_1(self):
        mock_input = ['3 1 1', '1 2 1']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask369ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_369A_acceptance_2(self):
        mock_input = ['4 3 1', '1 1 1 1']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask369ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_369A_acceptance_3(self):
        mock_input = ['3 1 2', '2 2 2']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask369ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_369A_acceptance_4(self):
        mock_input = ['8 2 2', '1 2 1 2 1 2 1 2']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask369ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
