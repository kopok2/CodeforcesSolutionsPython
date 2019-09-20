import unittest
from unittest.mock import patch

from cdf_382A import CodeforcesTask382ASolution


class TestCDF382A(unittest.TestCase):
    def test_382A_acceptance_1(self):
        mock_input = ['AC|T', 'L']
        expected = 'AC|TL'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask382ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_382A_acceptance_2(self):
        mock_input = ['|ABC', 'XYZ']
        expected = 'XYZ|ABC'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask382ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_382A_acceptance_3(self):
        mock_input = ['W|T', 'F']
        expected = 'Impossible'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask382ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_382A_acceptance_4(self):
        mock_input = ['ABC|', 'D']
        expected = 'Impossible'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask382ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
