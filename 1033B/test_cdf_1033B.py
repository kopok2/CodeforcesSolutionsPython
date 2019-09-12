import unittest
from unittest.mock import patch

from cdf_1033B import CodeforcesTask1033BSolution


class TestCDF1033B(unittest.TestCase):
    def test_1033B_acceptance_1(self):
        mock_input = ['4', '6 5', '16 13', '61690850361 24777622630', '34 33']
        expected = 'YES\nNO\nNO\nYES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1033BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
