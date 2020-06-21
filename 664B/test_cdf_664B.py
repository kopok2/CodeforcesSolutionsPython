import unittest
from unittest.mock import patch

from cdf_664B import CodeforcesTask664BSolution


class TestCDF664B(unittest.TestCase):
    def test_664B_acceptance_1(self):
        mock_input = ['? + ? - ? + ? + ? = 42']
        expected = 'Possible\n9 + 13 - 39 + 28 + 31 = 42'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask664BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_664B_acceptance_2(self):
        mock_input = ['? - ? = 1']
        expected = 'Impossible'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask664BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_664B_acceptance_3(self):
        mock_input = ['? = 1000000']
        expected = 'Possible\n1000000 = 1000000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask664BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
