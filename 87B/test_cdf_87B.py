import unittest
from unittest.mock import patch

from cdf_87B import CodeforcesTask87BSolution


class TestCDF87B(unittest.TestCase):
    def test_87B_acceptance_1(self):
        mock_input = ['5', 'typedef void* ptv', 'typeof ptv', 'typedef &&ptv node', 'typeof node', 'typeof &ptv']
        expected = 'void*\nerrtype\nvoid'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask87BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_87B_acceptance_2(self):
        mock_input = ['17', 'typedef void* b', 'typedef b* c', 'typeof b', 'typeof c', 'typedef &b b', 'typeof b', 'typeof c', 'typedef &&b* c', 'typeof c', 'typedef &b* c', 'typeof c', 'typedef &void b', 'typeof b', 'typedef b******* c', 'typeof c', 'typedef &&b* c', 'typeof c']
        expected = 'void*\nvoid**\nvoid\nvoid**\nerrtype\nvoid\nerrtype\nerrtype\nerrtype'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask87BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
