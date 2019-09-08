class CodeforcesTask1063ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.word = ''

    def read_input(self):
        self.n = int(input())
        self.word = input()

    def process_task(self):
        self.result = "".join(sorted(list(self.word)))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1063ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
