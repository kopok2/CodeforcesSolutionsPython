import unittest
from unittest.mock import patch

from cdf_269B import CodeforcesTask269BSolution


class TestCDF269B(unittest.TestCase):
    def test_269B_acceptance_1(self):
        mock_input = ['3 2', '2 1', '1 2.0', '1 3.100']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask269BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_269B_acceptance_2(self):
        mock_input = ['3 3', '1 5.0', '2 5.5', '3 6.0']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask269BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_269B_acceptance_3(self):
        mock_input = ['6 3', '1 14.284235', '2 17.921382', '1 20.328172', '3 20.842331', '1 25.790145', '1 27.204125']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask269BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
