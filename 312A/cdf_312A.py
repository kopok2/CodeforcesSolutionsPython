class CodeforcesTask312ASolution:
    def __init__(self):
        self.result = ''
        self.mess_count = 0
        self.messages = []

    def read_input(self):
        self.mess_count = int(input())
        self.messages = [input() for x in range(self.mess_count)]

    def process_task(self):
        for message in self.messages:
            if message[:5] == "miao.":
                if message[-5:] == "lala.":
                    self.result += "OMG>.< I don't know!\n"
                else:
                    self.result += "Rainbow's\n"
            else:
                if message[-5:] == "lala.":
                    self.result += "Freda's\n"
                else:
                    self.result += "OMG>.< I don't know!\n"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask312ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
