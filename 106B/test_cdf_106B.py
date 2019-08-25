import unittest
from unittest.mock import patch

from cdf_106B import CodeforcesTask106BSolution


class TestCDF106B(unittest.TestCase):
    def test_106B_acceptance_1(self):
        mock_input = ['5', '2100 512 150 200', '2000 2048 240 350', '2300 1024 200 320', '2500 2048 80 300', '2000 512 180 150']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask106BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
