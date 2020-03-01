import unittest
from unittest.mock import patch

from cdf_713A import CodeforcesTask713ASolution


class TestCDF713A(unittest.TestCase):
    def test_713A_acceptance_1(self):
        mock_input = ['12', '+ 1', '+ 241', '? 1', '+ 361', '- 241', '? 0101', '+ 101', '? 101', '- 101', '? 101', '+ 4000', '? 0']
        expected = '2\n1\n2\n1\n1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask713ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_713A_acceptance_2(self):
        mock_input = ['4', '+ 200', '+ 200', '- 200', '? 0']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask713ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
