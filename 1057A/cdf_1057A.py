class CodeforcesTask1057ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.routers = []

    def read_input(self):
        self.n = int(input())
        self.routers = [int(x) for x in input().split(" ")]

    def process_task(self):
        s = [self.n]
        x = self.n
        while x != 1:
            step = self.routers[x - 2]
            x = step
            s.append(step)
        while s:
            print(s.pop(-1), end=" ")

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1057ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
