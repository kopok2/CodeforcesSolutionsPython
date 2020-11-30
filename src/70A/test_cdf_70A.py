import unittest
from unittest.mock import patch

from cdf_70A import CodeforcesTask70ASolution


class TestCDF70A(unittest.TestCase):
    def test_70A_acceptance_1(self):
        mock_input = ['3']
        expected = '9'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask70ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
