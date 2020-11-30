import unittest
from unittest.mock import patch

from cdf_327B import CodeforcesTask327BSolution


class TestCDF327B(unittest.TestCase):
    def test_327B_acceptance_1(self):
        mock_input = ['3']
        expected = '2 9 15'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask327BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_327B_acceptance_2(self):
        mock_input = ['5']
        expected = '11 14 20 27 31'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask327BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
