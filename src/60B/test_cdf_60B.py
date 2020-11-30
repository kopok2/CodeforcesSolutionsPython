import unittest
from unittest.mock import patch

from cdf_60B import CodeforcesTask60BSolution


class TestCDF60B(unittest.TestCase):
    def test_60B_acceptance_1(self):
        mock_input = ['1 1 1', '', '.', '', '1 1']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask60BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_60B_acceptance_2(self):
        mock_input = ['2 1 1', '', '.', '', '#', '', '1 1']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask60BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_60B_acceptance_3(self):
        mock_input = ['2 2 2', '', '.#', '##', '', '..', '..', '', '1 1']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask60BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_60B_acceptance_4(self):
        mock_input = ['3 2 2', '', '#.', '##', '', '#.', '.#', '', '..', '..', '', '1 2']
        expected = '7'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask60BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_60B_acceptance_5(self):
        mock_input = ['3 3 3', '', '.#.', '###', '##.', '', '.##', '###', '##.', '', '...', '...', '...', '', '1 1']
        expected = '13'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask60BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
