    def test_{0}_acceptance_{1}(self):
        mock_input = {2}
        expected = '{3}'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask{0}Solution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

