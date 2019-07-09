import unittest
from cdf_2a import add_score


class Cdf2ATest(unittest.TestCase):
    def test_add_score(self):
        self.assertEqual(add_score({'leading': '', 'leader_highest': 0}, "mike 2"), {'mike': 2, 'leading': 'mike',
                                                                                     'leader_highest': 0})
        self.assertEqual(add_score({'mike': 2, 'leading': 'mike'}, "jane -1"), {'mike': 2, 'jane': 0,
                                                                                'leading': 'mike', 'leader_highest': 0})
        board = {'leading': '', 'leader_highest': 0}
        board = add_score(board, "mike 3")
        board = add_score(board, "andrew 5")
        board = add_score(board, "mike 2")
        self.assertEqual(board["leading"], "andrew")
        board = {'leading': '', 'leader_highest': 0}
        board = add_score(board, "andrew 3")
        board = add_score(board, "andrew 2")
        board = add_score(board, "mike 2")
        self.assertEqual(board["leading"], "andrew")


if __name__ == "__main__":
    unittest.main()
