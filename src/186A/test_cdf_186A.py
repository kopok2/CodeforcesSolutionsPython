import unittest
from unittest.mock import patch

from cdf_186A import CodeforcesTask186ASolution


class TestCDF186A(unittest.TestCase):
    def test_186A_acceptance_1(self):
        mock_input = ['ab', 'ba']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask186ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_186A_acceptance_2(self):
        mock_input = ['aa', 'ab']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask186ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
