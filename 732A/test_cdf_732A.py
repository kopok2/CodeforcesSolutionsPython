import unittest
from unittest.mock import patch

from cdf_732A import CodeforcesTask732ASolution


class TestCDF732A(unittest.TestCase):
    def test_732A_acceptance_1(self):
        mock_input = ['117 3']
        expected = '9'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask732ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_732A_acceptance_2(self):
        mock_input = ['237 7']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask732ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_732A_acceptance_3(self):
        mock_input = ['15 2']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask732ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
