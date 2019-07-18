import unittest
from unittest.mock import patch

from cdf_373A import CodeforcesTask373ASolution


class TestCDF373A(unittest.TestCase):
    def test_373A_acceptance_1(self):
        mock_input = ['1', '.135', '1247', '3468', '5789']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask373ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_373A_acceptance_2(self):
        mock_input = ['5', '..1.', '1111', '..1.', '..1.']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask373ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_373A_acceptance_3(self):
        mock_input = ['1', '....', '12.1', '.2..', '.2..']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask373ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
