import unittest
from unittest.mock import patch

from cdf_462B import CodeforcesTask462BSolution


class TestCDF462B(unittest.TestCase):
    def test_462B_acceptance_1(self):
        mock_input = ['15 10', 'DZFDFZDFDDDDDDF']
        expected = '82'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask462BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_462B_acceptance_2(self):
        mock_input = ['6 4', 'YJSNPI']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask462BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
