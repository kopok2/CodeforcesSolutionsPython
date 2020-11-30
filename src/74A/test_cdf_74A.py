import unittest
from unittest.mock import patch

from cdf_74A import CodeforcesTask74ASolution


class TestCDF74A(unittest.TestCase):
    def test_74A_acceptance_1(self):
        mock_input = ['5', 'Petr 3 1 490 920 1000 1200 0', 'tourist 2 0 490 950 1100 1400 0', 'Egor 7 0 480 900 950 0 1000', 'c00lH4x0R 0 10 150 0 0 0 0', 'some_participant 2 1 450 720 900 0 0']
        expected = 'tourist'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask74ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
