import unittest
from unittest.mock import patch

from cdf_907B import CodeforcesTask907BSolution


class TestCDF907B(unittest.TestCase):
    def test_907B_acceptance_1(self):
        mock_input = ['... ... ...', '... ... ...', '... ... ...', '', '... ... ...', '... ... ...', '... x.. ...', '', '... ... ...', '... ... ...', '... ... ...', '6 4']
        expected = '... ... ...\n... ... ...\n... ... ...\n\n... ... ...\n... ... ...\n... x.. ...\n\n!!! ... ...\n!!! ... ...\n!!! ... ...'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask907BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_907B_acceptance_2(self):
        mock_input = ['xoo x.. x..', 'ooo ... ...', 'ooo ... ...', '', 'x.. x.. x..', '... ... ...', '... ... ...', '', 'x.. x.. x..', '... ... ...', '... ... ...', '7 4']
        expected = 'xoo x!! x!!\nooo !!! !!!\nooo !!! !!!\n\nx!! x!! x!!\n!!! !!! !!!\n!!! !!! !!!\n\nx!! x!! x!!\n!!! !!! !!!\n!!! !!! !!!'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask907BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_907B_acceptance_3(self):
        mock_input = ['o.. ... ...', '... ... ...', '... ... ...', '', '... xxx ...', '... xox ...', '... ooo ...', '', '... ... ...', '... ... ...', '... ... ...', '5 5']
        expected = 'o!! !!! !!!\n!!! !!! !!!\n!!! !!! !!!\n\n!!! xxx !!!\n!!! xox !!!\n!!! ooo !!!\n\n!!! !!! !!!\n!!! !!! !!!\n!!! !!! !!!'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask907BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
