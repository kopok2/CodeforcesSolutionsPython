import unittest
from unittest.mock import patch

from cdf_335A import CodeforcesTask335ASolution


class TestCDF335A(unittest.TestCase):
    def test_335A_acceptance_1(self):
        mock_input = ['banana', '4']
        expected = '2\nbaan'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask335ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_335A_acceptance_2(self):
        mock_input = ['banana', '3']
        expected = '3\nnab'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask335ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_335A_acceptance_3(self):
        mock_input = ['banana', '2']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask335ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
