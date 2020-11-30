import unittest
from unittest.mock import patch

from cdf_705B import CodeforcesTask705BSolution


class TestCDF705B(unittest.TestCase):
    def test_705B_acceptance_1(self):
        mock_input = ['3', '1 2 3']
        expected = '2\n1\n1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask705BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_705B_acceptance_2(self):
        mock_input = ['5', '1 1 5 1 1']
        expected = '2\n2\n2\n2\n2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask705BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
