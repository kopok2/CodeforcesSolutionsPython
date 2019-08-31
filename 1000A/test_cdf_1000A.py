import unittest
from unittest.mock import patch

from cdf_1000A import CodeforcesTask1000ASolution


class TestCDF1000A(unittest.TestCase):
    def test_1000A_acceptance_1(self):
        mock_input = ['3', 'XS', 'XS', 'M', 'XL', 'S', 'XS']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1000ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1000A_acceptance_2(self):
        mock_input = ['2', 'XXXL', 'XXL', 'XXL', 'XXXS']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1000ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1000A_acceptance_3(self):
        mock_input = ['2', 'M', 'XS', 'XS', 'M']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1000ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
