import unittest
from unittest.mock import patch

from cdf_664A import CodeforcesTask664ASolution


class TestCDF664A(unittest.TestCase):
    def test_664A_acceptance_1(self):
        mock_input = ['1 2']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask664ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_664A_acceptance_2(self):
        mock_input = ['61803398874989484820458683436563811772030917980576 61803398874989484820458683436563811772030917980576']
        expected = '61803398874989484820458683436563811772030917980576'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask664ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
