class CodeforcesTask281ASolution:
    def __init__(self):
        self.result = ''
        self.s = ''

    def read_input(self):
        self.s = input()

    def process_task(self):
        self.result = self.s[:1].upper() + self.s[1:]

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask281ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
