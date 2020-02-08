import unittest
from unittest.mock import patch

from cdf_546A import CodeforcesTask546ASolution


class TestCDF546A(unittest.TestCase):
    def test_546A_acceptance_1(self):
        mock_input = ['3 17 4']
        expected = '13'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask546ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
