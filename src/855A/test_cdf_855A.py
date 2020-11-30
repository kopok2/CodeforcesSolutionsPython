import unittest
from unittest.mock import patch

from cdf_855A import CodeforcesTask855ASolution


class TestCDF855A(unittest.TestCase):
    def test_855A_acceptance_1(self):
        mock_input = ['6', 'tom', 'lucius', 'ginny', 'harry', 'ginny', 'harry']
        expected = 'NO\nNO\nNO\nNO\nYES\nYES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask855ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_855A_acceptance_2(self):
        mock_input = ['3', 'a', 'a', 'a']
        expected = 'NO\nYES\nYES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask855ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
