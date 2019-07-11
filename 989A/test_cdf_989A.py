import unittest
from unittest.mock import patch

from cdf_989A import CodeforcesTask989ASolution


class TestCDF989A(unittest.TestCase):
    def test_989A_acceptance_1(self):
        mock_input = ['.BAC.']
        expected = 'Yes'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask989ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_989A_acceptance_2(self):
        mock_input = ['AA..CB']
        expected = 'No'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask989ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
