import unittest
from unittest.mock import patch

from cdf_426A import CodeforcesTask426ASolution


class TestCDF426A(unittest.TestCase):
    def test_426A_acceptance_1(self):
        mock_input = ['3 4', '1 1 1']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask426ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_426A_acceptance_2(self):
        mock_input = ['3 4', '3 1 3']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask426ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_426A_acceptance_3(self):
        mock_input = ['3 4', '4 4 4']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask426ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
