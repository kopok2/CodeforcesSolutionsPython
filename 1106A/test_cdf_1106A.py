import unittest
from unittest.mock import patch

from cdf_1106A import CodeforcesTask1106ASolution


class TestCDF1106A(unittest.TestCase):
    def test_1106A_acceptance_1(self):
        mock_input = ['5 ..... .XXX. .XXX. .XXX. .....']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1106ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1106A_acceptance_2(self):
        mock_input = ['2 XX XX']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1106ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1106A_acceptance_3(self):
        mock_input = ['6 ...... X.X.X. .X.X.X X.X.X. .X.X.X ......']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1106ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
