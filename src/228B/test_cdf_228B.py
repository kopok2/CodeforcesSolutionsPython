import unittest
from unittest.mock import patch

from cdf_228B import CodeforcesTask228BSolution


class TestCDF228B(unittest.TestCase):
    def test_228B_acceptance_1(self):
        mock_input = ['3 2', '01', '10', '00', '2 3', '001', '111']
        expected = '0 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask228BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_228B_acceptance_2(self):
        mock_input = ['3 3', '000', '010', '000', '1 1', '1']
        expected = '-1 -1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask228BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
