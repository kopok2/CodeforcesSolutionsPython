import unittest
from unittest.mock import patch

from cdf_894A import CodeforcesTask894ASolution


class TestCDF894A(unittest.TestCase):
    def test_894A_acceptance_1(self):
        mock_input = ['QAQAQYSYIOIWIN']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask894ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_894A_acceptance_2(self):
        mock_input = ['QAQQQZZYNOIWIN']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask894ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
