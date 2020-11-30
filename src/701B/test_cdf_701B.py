import unittest
from unittest.mock import patch

from cdf_701B import CodeforcesTask701BSolution


class TestCDF701B(unittest.TestCase):
    def test_701B_acceptance_1(self):
        mock_input = ['3 3', '1 1', '3 1', '2 2']
        expected = '4 2 0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask701BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_701B_acceptance_2(self):
        mock_input = ['5 2', '1 5', '5 1']
        expected = '16 9'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask701BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_701B_acceptance_3(self):
        mock_input = ['100000 1', '300 400']
        expected = '9999800001'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask701BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
