import unittest
from unittest.mock import patch

from cdf_837A import CodeforcesTask837ASolution


class TestCDF837A(unittest.TestCase):
    def test_837A_acceptance_1(self):
        mock_input = ['7', 'NonZERO']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask837ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_837A_acceptance_2(self):
        mock_input = ['24', 'this is zero answer text']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask837ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_837A_acceptance_3(self):
        mock_input = ['24', 'Harbour Space University']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask837ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
