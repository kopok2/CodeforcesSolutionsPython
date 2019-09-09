import unittest
from unittest.mock import patch

from cdf_209A import CodeforcesTask209ASolution


class TestCDF209A(unittest.TestCase):
    def test_209A_acceptance_1(self):
        mock_input = ['3']
        expected = '6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask209ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_209A_acceptance_2(self):
        mock_input = ['4']
        expected = '11'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask209ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
