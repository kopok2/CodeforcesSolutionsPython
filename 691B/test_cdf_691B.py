import unittest
from unittest.mock import patch

from cdf_691B import CodeforcesTask691BSolution


class TestCDF691B(unittest.TestCase):
    def test_691B_acceptance_1(self):
        mock_input = ['oXoxoXo']
        expected = 'TAK'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask691BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_691B_acceptance_2(self):
        mock_input = ['bod']
        expected = 'TAK'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask691BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_691B_acceptance_3(self):
        mock_input = ['ER']
        expected = 'NIE'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask691BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
