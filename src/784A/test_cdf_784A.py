import unittest
from unittest.mock import patch

from cdf_784A import CodeforcesTask784ASolution


class TestCDF784A(unittest.TestCase):
    def test_784A_acceptance_1(self):
        mock_input = ['3']
        expected = '27'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask784ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
