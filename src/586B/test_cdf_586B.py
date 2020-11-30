import unittest
from unittest.mock import patch

from cdf_586B import CodeforcesTask586BSolution


class TestCDF586B(unittest.TestCase):
    def test_586B_acceptance_1(self):
        mock_input = ['4', '1 2 3', '3 2 1', '3 2 2 3']
        expected = '12'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask586BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_586B_acceptance_2(self):
        mock_input = ['3', '1 2', '3 3', '2 1 3']
        expected = '11'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask586BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_586B_acceptance_3(self):
        mock_input = ['2', '1', '1', '1 1']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask586BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
