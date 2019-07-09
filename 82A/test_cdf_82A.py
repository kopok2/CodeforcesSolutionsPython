import unittest
from unittest.mock import patch

from cdf_82A import CodeforcesTask82ASolution


class TestCDF82A(unittest.TestCase):
    def test_82A_acceptance_1(self):
        mock_input = ['1']
        expected = 'Sheldon'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask82ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_82A_acceptance_2(self):
        mock_input = ['6']
        expected = 'Sheldon'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask82ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_82A_acceptance_3(self):
        mock_input = ['1802']
        expected = 'Penny'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask82ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
