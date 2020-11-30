import unittest
from unittest.mock import patch

from cdf_245B import CodeforcesTask245BSolution


class TestCDF245B(unittest.TestCase):
    def test_245B_acceptance_1(self):
        mock_input = ['httpsunrux']
        expected = 'http://sun.ru/x'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask245BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_245B_acceptance_2(self):
        mock_input = ['ftphttprururu']
        expected = 'ftp://http.ru/ruru'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask245BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
