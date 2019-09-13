import unittest
from unittest.mock import patch

from cdf_189A import CodeforcesTask189ASolution


class TestCDF189A(unittest.TestCase):
    def test_189A_acceptance_1(self):
        mock_input = ['5 5 3 2']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask189ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_189A_acceptance_2(self):
        mock_input = ['7 5 5 2']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask189ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
