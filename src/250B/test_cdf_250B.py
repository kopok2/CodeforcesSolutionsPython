import unittest
from unittest.mock import patch

from cdf_250B import CodeforcesTask250BSolution


class TestCDF250B(unittest.TestCase):
    def test_250B_acceptance_1(self):
        mock_input = ['6', 'a56f:d3:0:0124:01:f19a:1000:00', 'a56f:00d3:0000:0124:0001::', 'a56f::0124:0001:0000:1234:0ff0', 'a56f:0000::0000:0001:0000:1234:0ff0', '::', '0ea::4d:f4:6:0']
        expected = 'a56f:00d3:0000:0124:0001:f19a:1000:0000\na56f:00d3:0000:0124:0001:0000:0000:0000\na56f:0000:0000:0124:0001:0000:1234:0ff0\na56f:0000:0000:0000:0001:0000:1234:0ff0\n0000:0000:0000:0000:0000:0000:0000:0000\n00ea:0000:0000:0000:004d:00f4:0006:0000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask250BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
