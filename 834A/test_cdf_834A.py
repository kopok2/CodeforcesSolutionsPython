import unittest
from unittest.mock import patch

from cdf_834A import CodeforcesTask834ASolution


class TestCDF834A(unittest.TestCase):
    def test_834A_acceptance_1(self):
        mock_input = ['^ >', '1']
        expected = 'cw'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask834ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_834A_acceptance_2(self):
        mock_input = ['< ^', '3']
        expected = 'ccw'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask834ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_834A_acceptance_3(self):
        mock_input = ['^ v', '6']
        expected = 'undefined'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask834ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
