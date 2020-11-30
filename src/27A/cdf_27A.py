class CodeforcesTask27ASolution:
    def __init__(self):
        self.result = ''
        self.used = []

    def read_input(self):
        input()
        self.used = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.used.sort()
        self.result = str(len(self.used) + 1)
        for x in range(len(self.used)):
            if self.used[x] != x + 1:
                self.result = str(x + 1)
                break

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask27ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
