import unittest
from unittest.mock import patch

from cdf_454A import CodeforcesTask454ASolution


class TestCDF454A(unittest.TestCase):
    def test_454A_acceptance_1(self):
        mock_input = ['3']
        expected = '*D*\nDDD\n*D*'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask454ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_454A_acceptance_2(self):
        mock_input = ['5']
        expected = '**D**\n*DDD*\nDDDDD\n*DDD*\n**D**'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask454ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_454A_acceptance_3(self):
        mock_input = ['7']
        expected = '***D***\n**DDD**\n*DDDDD*\nDDDDDDD\n*DDDDD*\n**DDD**\n***D***'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask454ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
