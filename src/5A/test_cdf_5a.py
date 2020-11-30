import unittest
from cdf_5a import Chat


class TestCDF5A(unittest.TestCase):
    def test_add_user(self):
        chat = Chat()
        chat.add_user("dmitry")
        chat.add_user("sasha")
        self.assertEqual(chat.users, ["dmitry", "sasha"])

    def test_remove_user(self):
        chat = Chat()
        chat.add_user("dmitry")
        chat.add_user("sasha")
        chat.remove_user("sasha")
        self.assertEqual(chat.users, ["dmitry"])

    def test_send_msg(self):
        chat = Chat()
        chat.users = ["dmitry", "sasha"]
        chat.send_msg("hi")
        self.assertEqual(chat.bytes_sent, 4)

    def test_process_cmd(self):
        chat = Chat()
        chat.process_cmd("+dmitry")
        chat.process_cmd("+sasha")
        self.assertEqual(chat.users, ["dmitry", "sasha"])
        chat.process_cmd("-dmitry")
        self.assertEqual(chat.users, ["sasha"])
        chat.process_cmd("sasha:hi")
        self.assertEqual(chat.bytes_sent, 2)
        chat.process_cmd("+dmitry")
        chat.process_cmd("sasha:hi")
        self.assertEqual(chat.bytes_sent, 6)


if __name__ == "__main__":
    unittest.main()
