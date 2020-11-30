import unittest
from unittest.mock import patch

from cdf_151B import CodeforcesTask151BSolution


class TestCDF151B(unittest.TestCase):
    def test_151B_acceptance_1(self):
        mock_input = ['4', '2 Fedorov', '22-22-22', '98-76-54', '3 Melnikov', '75-19-09', '23-45-67', '99-99-98', '7 Rogulenko', '22-22-22', '11-11-11', '33-33-33', '44-44-44', '55-55-55', '66-66-66', '95-43-21', '3 Kaluzhin', '11-11-11', '99-99-99', '98-65-32']
        expected = 'If you want to call a taxi, you should call: Rogulenko.\nIf you want to order a pizza, you should call: Fedorov, Rogulenko, Kaluzhin.\nIf you want to go to a cafe with a wonderful girl, you should call: Melnikov.'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask151BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_151B_acceptance_2(self):
        mock_input = ['3', '5 Gleb', '66-66-66', '55-55-55', '01-01-01', '65-43-21', '12-34-56', '3 Serega', '55-55-55', '87-65-43', '65-55-21', '5 Melnik', '12-42-12', '87-73-01', '36-04-12', '88-12-22', '82-11-43']
        expected = 'If you want to call a taxi, you should call: Gleb.\nIf you want to order a pizza, you should call: Gleb, Serega.\nIf you want to go to a cafe with a wonderful girl, you should call: Melnik.'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask151BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_151B_acceptance_3(self):
        mock_input = ['3', '3 Kulczynski', '22-22-22', '65-43-21', '98-12-00', '4 Pachocki', '11-11-11', '11-11-11', '11-11-11', '98-76-54', '0 Smietanka']
        expected = 'If you want to call a taxi, you should call: Pachocki.\nIf you want to order a pizza, you should call: Kulczynski, Pachocki.\nIf you want to go to a cafe with a wonderful girl, you should call: Kulczynski.'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask151BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
