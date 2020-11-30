import unittest
from unittest.mock import patch

from cdf_477B import CodeforcesTask477BSolution


class TestCDF477B(unittest.TestCase):
    def test_477B_acceptance_1(self):
        mock_input = ['1 1']
        expected = '5\n1 2 3 5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask477BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_477B_acceptance_2(self):
        mock_input = ['2 2']
        expected = '22\n2 4 6 22\n14 18 10 16'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask477BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
