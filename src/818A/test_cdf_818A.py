import unittest
from unittest.mock import patch

from cdf_818A import CodeforcesTask818ASolution


class TestCDF818A(unittest.TestCase):
    def test_818A_acceptance_1(self):
        mock_input = ['18 2']
        expected = '3 6 9'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask818ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_818A_acceptance_2(self):
        mock_input = ['9 10']
        expected = '0 0 9'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask818ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_818A_acceptance_3(self):
        mock_input = ['1000000000000 5']
        expected = '83333333333 416666666665 500000000002'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask818ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_818A_acceptance_4(self):
        mock_input = ['1000000000000 499999999999']
        expected = '1 499999999999 500000000000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask818ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
