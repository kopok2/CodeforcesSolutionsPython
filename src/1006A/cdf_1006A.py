class CodeforcesTask1006ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.sequence = []

    def read_input(self):
        self.n = int(input())
        self.sequence = [int(x) for x in input().split(" ")]

    def process_task(self):
        result = [((x - 1) // 2) * 2 + 1 for x in self.sequence]
        self.result = " ".join([str(x) for x in result])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1006ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
