import unittest
from unittest.mock import patch

from cdf_312A import CodeforcesTask312ASolution


class TestCDF312A(unittest.TestCase):
    def test_312A_acceptance_1(self):
        mock_input = ['5', 'I will go to play with you lala.', 'wow, welcome.', 'miao.lala.', 'miao.', 'miao .']
        expected = 'Freda's\nOMG>.< I don't know!\nOMG>.< I don't know!\nRainbow's\nOMG>.< I don't know!'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask312ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
