import unittest
from unittest.mock import patch

from cdf_330A import CodeforcesTask330ASolution


class TestCDF330A(unittest.TestCase):
    def test_330A_acceptance_1(self):
        mock_input = ['3 4', 'S...', '....', '..S.']
        expected = '8'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask330ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
