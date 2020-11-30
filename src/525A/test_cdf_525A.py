import unittest
from unittest.mock import patch

from cdf_525A import CodeforcesTask525ASolution


class TestCDF525A(unittest.TestCase):
    def test_525A_acceptance_1(self):
        mock_input = ['3', 'aAbB']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask525ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_525A_acceptance_2(self):
        mock_input = ['4', 'aBaCaB']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask525ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_525A_acceptance_3(self):
        mock_input = ['5', 'xYyXzZaZ']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask525ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
