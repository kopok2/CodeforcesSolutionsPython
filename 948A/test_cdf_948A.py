import unittest
from unittest.mock import patch

from cdf_948A import CodeforcesTask948ASolution


class TestCDF948A(unittest.TestCase):
    def test_948A_acceptance_1(self):
        mock_input = ['6 6', '..S...', '..S.W.', '.S....', '..W...', '...W..', '......']
        expected = 'Yes\n..SD..\n..SDW.\n.SD...\n.DW...\nDD.W..\n......'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask948ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_948A_acceptance_2(self):
        mock_input = ['1 2', 'SW']
        expected = 'No'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask948ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_948A_acceptance_3(self):
        mock_input = ['5 5', '.S...', '...S.', 'S....', '...S.', '.S...']
        expected = 'Yes\n.S...\n...S.\nS.D..\n...S.\n.S...'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask948ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
