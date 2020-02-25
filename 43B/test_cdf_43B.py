import unittest
from unittest.mock import patch

from cdf_43B import CodeforcesTask43BSolution


class TestCDF43B(unittest.TestCase):
    def test_43B_acceptance_1(self):
        mock_input = ['Instead of dogging Your footsteps it disappears but you dont notice anything', 'where is your dog']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask43BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_43B_acceptance_2(self):
        mock_input = ['Instead of dogging Your footsteps it disappears but you dont notice anything', 'Your dog is upstears']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask43BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_43B_acceptance_3(self):
        mock_input = ['Instead of dogging your footsteps it disappears but you dont notice anything', 'Your dog is upstears']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask43BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_43B_acceptance_4(self):
        mock_input = ['abcdefg hijk', 'k j i h g f e d c b a']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask43BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
