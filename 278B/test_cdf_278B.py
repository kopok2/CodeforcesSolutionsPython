import unittest
from unittest.mock import patch

from cdf_278B import CodeforcesTask278BSolution


class TestCDF278B(unittest.TestCase):
    def test_278B_acceptance_1(self):
        mock_input = ['5', 'threehorses', 'goodsubstrings', 'secret', 'primematrix', 'beautifulyear']
        expected = 'j'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask278BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_278B_acceptance_2(self):
        mock_input = ['4', 'aa', 'bdefghijklmn', 'opqrstuvwxyz', 'c']
        expected = 'ab'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask278BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
