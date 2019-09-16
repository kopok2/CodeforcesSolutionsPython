import unittest
from unittest.mock import patch

from cdf_659B import CodeforcesTask659BSolution


class TestCDF659B(unittest.TestCase):
    def test_659B_acceptance_1(self):
        mock_input = ['5 2', 'Ivanov 1 763', 'Andreev 2 800', 'Petrov 1 595', 'Sidorov 1 790', 'Semenov 2 503']
        expected = 'Sidorov Ivanov\nAndreev Semenov'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask659BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_659B_acceptance_2(self):
        mock_input = ['5 2', 'Ivanov 1 800', 'Andreev 2 763', 'Petrov 1 800', 'Sidorov 1 800', 'Semenov 2 503']
        expected = '?\nAndreev Semenov'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask659BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
