import unittest
from unittest.mock import patch

from cdf_865A import CodeforcesTask865ASolution


class TestCDF865A(unittest.TestCase):
    def test_865A_acceptance_1(self):
        mock_input = ['18']
        expected = '30 4\n1 5 10 25'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask865ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_865A_acceptance_2(self):
        mock_input = ['3']
        expected = '20 2\n5 2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask865ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_865A_acceptance_3(self):
        mock_input = ['314']
        expected = '183 4\n6 5 2 139'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask865ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
