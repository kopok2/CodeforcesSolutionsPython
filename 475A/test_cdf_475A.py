import unittest
from unittest.mock import patch

from cdf_475A import CodeforcesTask475ASolution


class TestCDF475A(unittest.TestCase):
    def test_475A_acceptance_1(self):
        mock_input = ['9']
        expected = '+------------------------+\n|O.O.O.#.#.#.#.#.#.#.#.|D|)\n|O.O.O.#.#.#.#.#.#.#.#.|.|\n|O.......................|\n|O.O.#.#.#.#.#.#.#.#.#.|.|)\n+------------------------+'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask475ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_475A_acceptance_2(self):
        mock_input = ['20']
        expected = '+------------------------+\n|O.O.O.O.O.O.O.#.#.#.#.|D|)\n|O.O.O.O.O.O.#.#.#.#.#.|.|\n|O.......................|\n|O.O.O.O.O.O.#.#.#.#.#.|.|)\n+------------------------+'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask475ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
