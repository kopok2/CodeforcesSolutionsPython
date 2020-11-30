import unittest
from unittest.mock import patch

from cdf_25B import CodeforcesTask25BSolution


class TestCDF25B(unittest.TestCase):
    def test_25B_acceptance_1(self):
        mock_input = ['6', '549871']
        expected = '54-98-71'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask25BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_25B_acceptance_2(self):
        mock_input = ['7', '1198733']
        expected = '11-987-33'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask25BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
