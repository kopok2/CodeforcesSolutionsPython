import unittest
from unittest.mock import patch

from cdf_898B import CodeforcesTask898BSolution


class TestCDF898B(unittest.TestCase):
    def test_898B_acceptance_1(self):
        mock_input = ['7', '2', '3']
        expected = 'YES\n2 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask898BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_898B_acceptance_2(self):
        mock_input = ['100', '25', '10']
        expected = 'YES\n0 10'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask898BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_898B_acceptance_3(self):
        mock_input = ['15', '4', '8']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask898BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_898B_acceptance_4(self):
        mock_input = ['9960594', '2551', '2557']
        expected = 'YES\n1951 1949'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask898BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
