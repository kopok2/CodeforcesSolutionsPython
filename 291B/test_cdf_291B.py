import unittest
from unittest.mock import patch

from cdf_291B import CodeforcesTask291BSolution


class TestCDF291B(unittest.TestCase):
    def test_291B_acceptance_1(self):
        mock_input = ['"RUn.exe O" "" " 2ne, " two! . " "']
        expected = '<RUn.exe O>\n<>\n< 2ne, >\n<two!>\n<.>\n< >'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask291BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_291B_acceptance_2(self):
        mock_input = ['firstarg second ""']
        expected = '<firstarg>\n<second>\n<>'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask291BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
