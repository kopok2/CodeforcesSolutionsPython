import unittest
from unittest.mock import patch

from cdf_27A import CodeforcesTask27ASolution


class TestCDF27A(unittest.TestCase):
    def test_27A_acceptance_1(self):
        mock_input = ['3', '1 7 2']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask27ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
