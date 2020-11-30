import unittest
from unittest.mock import patch

from cdf_114A import CodeforcesTask114ASolution


class TestCDF114A(unittest.TestCase):
    def test_114A_acceptance_1(self):
        mock_input = ['5', '25']
        expected = 'YES\n1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask114ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_114A_acceptance_2(self):
        mock_input = ['3', '8']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask114ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
