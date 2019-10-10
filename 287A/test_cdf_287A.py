import unittest
from unittest.mock import patch

from cdf_287A import CodeforcesTask287ASolution


class TestCDF287A(unittest.TestCase):
    def test_287A_acceptance_1(self):
        mock_input = ['####', '.#..', '####', '....']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask287ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_287A_acceptance_2(self):
        mock_input = ['####', '....', '####', '....']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask287ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
