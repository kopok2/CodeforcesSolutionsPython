import unittest
from unittest.mock import patch

from cdf_1103B import CodeforcesTask1103BSolution


class TestCDF1103B(unittest.TestCase):
    def test_1103B_acceptance_1(self):
        mock_input = ['start x x start x x y start x x y y end']
        expected = '? 0 0 ? 10 1 ! 1 ? 0 0 ? 3 4 ? 2 5 ! 2 ? 2 4 ? 2 5 ? 3 10 ? 9 1 ! 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1103BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
