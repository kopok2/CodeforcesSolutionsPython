import unittest
from unittest.mock import patch

from cdf_496B import CodeforcesTask496BSolution


class TestCDF496B(unittest.TestCase):
    def test_496B_acceptance_1(self):
        mock_input = ['3', '579']
        expected = '024'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask496BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_496B_acceptance_2(self):
        mock_input = ['4', '2014']
        expected = '0142'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask496BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
