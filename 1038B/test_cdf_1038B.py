import unittest
from unittest.mock import patch

from cdf_1038B import CodeforcesTask1038BSolution


class TestCDF1038B(unittest.TestCase):
    def test_1038B_acceptance_1(self):
        mock_input = ['1']
        expected = 'No'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1038BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1038B_acceptance_2(self):
        mock_input = ['3']
        expected = 'Yes\n1 2\n2 1 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1038BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
