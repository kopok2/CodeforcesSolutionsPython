import unittest
from cdf_3b import Lorry


class TestCDF3B(unittest.TestCase):
    def test_add_load(self):
        lorry = Lorry(2)
        lorry.add_load(1, 2)
        lorry.add_load(2, 5)
        lorry.add_load(2, 5)
        self.assertEqual(lorry.load, [("1", 1, 2), ("2", 2, 5), ("3", 2, 5)])

    def test_merge_load(self):
        lorry = Lorry(2)
        lorry.load = [("1", 1, 2), ("2", 1, 5), ("3", 2, 5)]
        lorry.merge_load()
        self.assertEqual(lorry.load, [("2 1", 2, 7), ("3", 2, 5)])

    def test_get_best_kayak(self):
        lorry = Lorry(3)
        lorry.load = [("1", 1, 2), ("2", 1, 5), ("3", 2, 5)]
        self.assertEqual(lorry.get_best_kayak(), ("2", 1, 5))

    def test_get_best_load(self):
        lorry = Lorry(2)
        lorry.load = [("1", 1, 2), ("2", 1, 5), ("3", 2, 5)]
        self.assertEqual(lorry.get_best_load(), (7, "2 1"))


if __name__ == "__main__":
    unittest.main()
