import unittest
from unittest.mock import patch

from cdf_523A import CodeforcesTask523ASolution


class TestCDF523A(unittest.TestCase):
    def test_523A_acceptance_1(self):
        mock_input = ['3 2', '.*.', '.*.']
        expected = '....\n....\n****\n****\n....\n....'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask523ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_523A_acceptance_2(self):
        mock_input = ['9 20', '**.......', '****.....', '******...', '*******..', '..******.', '....****.', '......***', '*.....***', '*********', '*********', '*********', '*********', '....**...', '...****..', '..******.', '.********', '****..***', '***...***', '**.....**', '*.......*']
        expected = '********......**********........********\n********......**********........********\n********........********......********..\n********........********......********..\n..********......********....********....\n..********......********....********....\n..********......********..********......\n..********......********..********......\n....********....****************........\n....********....****************........\n....********....****************........\n....********....****************........\n......******************..**********....\n......******************..**********....\n........****************....**********..\n........****************....**********..\n............************......**********\n............************......**********'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask523ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
