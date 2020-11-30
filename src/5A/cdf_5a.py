class Chat:
    def __init__(self):
        self.users = []
        self.bytes_sent = 0

    def add_user(self, name):
        self.users.append(name)

    def remove_user(self, name):
        self.users.pop(self.users.index(name))

    def send_msg(self, msg):
        self.bytes_sent += len(msg) * len(self.users)

    def process_cmd(self, cmd):
        if "+" in cmd:
            self.add_user(cmd.split("+")[1])
        elif "-" in cmd:
            self.remove_user(cmd.split("-")[1])
        else:
            self.send_msg(cmd.split(":")[1])


if __name__ == "__main__":
    chat = Chat()
    while True:
        try:
            chat.process_cmd(input())
        except:
            break
    print(chat.bytes_sent)
