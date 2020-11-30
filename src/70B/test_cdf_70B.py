import unittest
from unittest.mock import patch

from cdf_70B import CodeforcesTask70BSolution


class TestCDF70B(unittest.TestCase):
    def test_70B_acceptance_1(self):
        mock_input = ['25', 'Hello. I am a little walrus.']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask70BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_70B_acceptance_2(self):
        mock_input = ['2', 'How are you?']
        expected = 'Impossible'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask70BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_70B_acceptance_3(self):
        mock_input = ['19', 'Hello! Do you like fish? Why?']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask70BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
