class CodeforcesTask1146ASolution:
    def __init__(self):
        self.result = ''
        self.s = ''

    def read_input(self):
        self.s = input()

    def process_task(self):
        a = self.s.count("a")
        if a > len(self.s) // 2:
            self.result = str(len(self.s))
        else:
            self.result = str(a * 2 - 1)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1146ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
