import unittest
from unittest.mock import patch

from cdf_729A import CodeforcesTask729ASolution


class TestCDF729A(unittest.TestCase):
    def test_729A_acceptance_1(self):
        mock_input = ['7', 'aogogob']
        expected = 'a***b'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask729ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_729A_acceptance_2(self):
        mock_input = ['13', 'ogogmgogogogo']
        expected = '***gmg***'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask729ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_729A_acceptance_3(self):
        mock_input = ['9', 'ogoogoogo']
        expected = '*********'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask729ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
