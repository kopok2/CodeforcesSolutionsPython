import unittest
from unittest.mock import patch

from cdf_61A import CodeforcesTask61ASolution


class TestCDF61A(unittest.TestCase):
    def test_61A_acceptance_1(self):
        mock_input = ['1010100', '0100101']
        expected = '1110001'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask61ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_61A_acceptance_2(self):
        mock_input = ['000', '111']
        expected = '111'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask61ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_61A_acceptance_3(self):
        mock_input = ['1110', '1010']
        expected = '0100'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask61ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_61A_acceptance_4(self):
        mock_input = ['01110', '01100']
        expected = '00010'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask61ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
