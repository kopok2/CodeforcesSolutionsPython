import unittest
from unittest.mock import patch

from cdf_979B import CodeforcesTask979BSolution


class TestCDF979B(unittest.TestCase):
    def test_979B_acceptance_1(self):
        mock_input = ['3', 'Kuroo', 'Shiro', 'Katie']
        expected = 'Kuro'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask979BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_979B_acceptance_2(self):
        mock_input = ['7', 'treasurehunt', 'threefriends', 'hiCodeforces']
        expected = 'Shiro'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask979BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_979B_acceptance_3(self):
        mock_input = ['1', 'abcabc', 'cbabac', 'ababca']
        expected = 'Katie'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask979BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_979B_acceptance_4(self):
        mock_input = ['15', 'foPaErcvJ', 'mZaxowpbt', 'mkuOlaHRE']
        expected = 'Draw'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask979BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
