class CodeforcesTask672BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.word = ''

    def read_input(self):
        self.n = int(input())
        self.word = input()

    def process_task(self):
        if self.n > 26:
            self.result = "-1"
        else:
            self.result = str(self.n - len(set([ord(c) for c in self.word])))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask672BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
