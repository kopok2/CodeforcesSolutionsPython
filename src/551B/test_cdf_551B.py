import unittest
from unittest.mock import patch

from cdf_551B import CodeforcesTask551BSolution


class TestCDF551B(unittest.TestCase):
    def test_551B_acceptance_1(self):
        mock_input = ['aaa', 'a', 'b']
        expected = 'aaa'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask551BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_551B_acceptance_2(self):
        mock_input = ['pozdravstaklenidodiri', 'niste', 'dobri']
        expected = 'nisteaadddiiklooprrvz'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask551BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_551B_acceptance_3(self):
        mock_input = ['abbbaaccca', 'ab', 'aca']
        expected = 'ababacabcc'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask551BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
