import unittest
from unittest.mock import patch

from cdf_115A import CodeforcesTask115ASolution


class TestCDF115A(unittest.TestCase):
    def test_115A_acceptance_1(self):
        mock_input = ['5', '-1', '1', '2', '1', '-1']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask115ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
