import unittest
from unittest.mock import patch

from cdf_1063A import CodeforcesTask1063ASolution


class TestCDF1063A(unittest.TestCase):
    def test_1063A_acceptance_1(self):
        mock_input = ['5', 'oolol']
        expected = 'ololo'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1063ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1063A_acceptance_2(self):
        mock_input = ['16', 'gagadbcgghhchbdf']
        expected = 'abccbaghghghgdfd'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1063ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
