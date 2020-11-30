import unittest
from unittest.mock import patch

from cdf_493B import CodeforcesTask493BSolution


class TestCDF493B(unittest.TestCase):
    def test_493B_acceptance_1(self):
        mock_input = ['5', '1', '2', '-3', '-4', '3']
        expected = 'second'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask493BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_493B_acceptance_2(self):
        mock_input = ['3', '-1', '-2', '3']
        expected = 'first'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask493BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_493B_acceptance_3(self):
        mock_input = ['2', '4', '-4']
        expected = 'second'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask493BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
