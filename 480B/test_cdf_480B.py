import unittest
from unittest.mock import patch

from cdf_480B import CodeforcesTask480BSolution


class TestCDF480B(unittest.TestCase):
    def test_480B_acceptance_1(self):
        mock_input = ['3 250 185 230', '0 185 250']
        expected = '1\n230'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask480BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_480B_acceptance_2(self):
        mock_input = ['4 250 185 230', '0 20 185 250']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask480BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_480B_acceptance_3(self):
        mock_input = ['2 300 185 230', '0 300']
        expected = '2\n185 230'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask480BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
