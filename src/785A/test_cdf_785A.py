import unittest
from unittest.mock import patch

from cdf_785A import CodeforcesTask785ASolution


class TestCDF785A(unittest.TestCase):
    def test_785A_acceptance_1(self):
        mock_input = ['4', 'Icosahedron', 'Cube', 'Tetrahedron', 'Dodecahedron']
        expected = '42'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask785ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_785A_acceptance_2(self):
        mock_input = ['3', 'Dodecahedron', 'Octahedron', 'Octahedron']
        expected = '28'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask785ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
