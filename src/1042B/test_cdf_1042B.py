import unittest
from unittest.mock import patch

from cdf_1042B import CodeforcesTask1042BSolution


class TestCDF1042B(unittest.TestCase):
    def test_1042B_acceptance_1(self):
        mock_input = ['4', '5 C', '6 B', '16 BAC', '4 A']
        expected = '15'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1042BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1042B_acceptance_2(self):
        mock_input = ['2', '10 AB', '15 BA']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1042BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1042B_acceptance_3(self):
        mock_input = ['5', '10 A', '9 BC', '11 CA', '4 A', '5 B']
        expected = '13'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1042BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1042B_acceptance_4(self):
        mock_input = ['6', '100 A', '355 BCA', '150 BC', '160 AC', '180 B', '190 CA']
        expected = '250'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1042BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1042B_acceptance_5(self):
        mock_input = ['2', '5 BA', '11 CB']
        expected = '16'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1042BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
