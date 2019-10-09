import unittest
from unittest.mock import patch

from cdf_755C import CodeforcesTask755CSolution


class TestCDF755C(unittest.TestCase):
    def test_755C_acceptance_1(self):
        mock_input = ['5', '2 1 5 3 3']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask755CSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_755C_acceptance_2(self):
        mock_input = ['1', '1']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask755CSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
