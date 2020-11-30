import unittest
from unittest.mock import patch

from cdf_655A import CodeforcesTask655ASolution


class TestCDF655A(unittest.TestCase):
    def test_655A_acceptance_1(self):
        mock_input = ['AB', 'XC', 'XB', 'AC']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask655ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_655A_acceptance_2(self):
        mock_input = ['AB', 'XC', 'AC', 'BX']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask655ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
