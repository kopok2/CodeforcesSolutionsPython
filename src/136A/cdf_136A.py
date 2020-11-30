class CodeforcesTask136ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.p = []

    def read_input(self):
        self.n = int(input())
        self.p = [int(x) for x in input().split(" ")]

    def process_task(self):
        given = [0] * self.n
        for x in range(self.n):
            given[self.p[x] - 1] = x + 1
        self.result = ' '.join([str(x) for x in given])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask136ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
