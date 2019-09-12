import unittest
from unittest.mock import patch

from cdf_748B import CodeforcesTask748BSolution


class TestCDF748B(unittest.TestCase):
    def test_748B_acceptance_1(self):
        mock_input = ['helloworld', 'ehoolwlroz']
        expected = '3\nh e\nl o\nd z'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask748BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_748B_acceptance_2(self):
        mock_input = ['hastalavistababy', 'hastalavistababy']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask748BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_748B_acceptance_3(self):
        mock_input = ['merrychristmas', 'christmasmerry']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask748BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
