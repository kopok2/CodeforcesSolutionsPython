import unittest
from unittest.mock import patch

from cdf_1144A import CodeforcesTask1144ASolution


class TestCDF1144A(unittest.TestCase):
    def test_1144A_acceptance_1(self):
        mock_input = ['8 fced xyz r dabcef az aa bad babc']
        expected = 'Yes Yes Yes Yes No No No No'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1144ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
