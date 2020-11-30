class CodeforcesTask946ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.sequence = []

    def read_input(self):
        self.n = int(input())
        self.sequence = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.result = str(sum([abs(x) for x in self.sequence]))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask946ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
