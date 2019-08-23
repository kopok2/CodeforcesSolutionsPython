import unittest
from unittest.mock import patch

from cdf_835A import CodeforcesTask835ASolution


class TestCDF835A(unittest.TestCase):
    def test_835A_acceptance_1(self):
        mock_input = ['5 1 2 1 2']
        expected = 'First'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask835ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_835A_acceptance_2(self):
        mock_input = ['3 3 1 1 1']
        expected = 'Second'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask835ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_835A_acceptance_3(self):
        mock_input = ['4 5 3 1 5']
        expected = 'Friendship'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask835ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
