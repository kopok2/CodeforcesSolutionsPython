import unittest
from unittest.mock import patch

from cdf_263B import CodeforcesTask263BSolution


class TestCDF263B(unittest.TestCase):
    def test_263B_acceptance_1(self):
        mock_input = ['4 3', '5 1 3 4']
        expected = '2 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask263BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_263B_acceptance_2(self):
        mock_input = ['3 1', '2 4 1']
        expected = '4 0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask263BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_263B_acceptance_3(self):
        mock_input = ['4 50', '5 1 10 2']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask263BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
