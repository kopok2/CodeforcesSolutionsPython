import unittest
from unittest.mock import patch

from cdf_154B import CodeforcesTask154BSolution


class TestCDF154B(unittest.TestCase):
    def test_154B_acceptance_1(self):
        mock_input = ['10 10', '+ 6', '+ 10', '+ 5', '- 10', '- 5', '- 6', '+ 10', '+ 3', '+ 6', '+ 3']
        expected = 'Success\nConflict with 6\nSuccess\nAlready off\nSuccess\nSuccess\nSuccess\nSuccess\nConflict with 10\nAlready on'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask154BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
