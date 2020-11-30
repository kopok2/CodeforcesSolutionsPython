import unittest
from unittest.mock import patch

from cdf_835B import CodeforcesTask835BSolution


class TestCDF835B(unittest.TestCase):
    def test_835B_acceptance_1(self):
        mock_input = ['3', '11']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask835BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_835B_acceptance_2(self):
        mock_input = ['3', '99']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask835BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
