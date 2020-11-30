class CodeforcesTask892BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.claws = []

    def read_input(self):
        self.n = int(input())
        self.claws = [int(x) for x in input().split(" ")]

    def process_task(self):
        kill = False
        living = 0
        kill_range = self.n + 1
        for x in range(self.n, 0, -1):
            if x < kill_range:
                kill = False
            if not kill:
                living += 1
            if self.claws[x - 1]:
                kill = True
                kill_range = min(kill_range, x - self.claws[x - 1])
        self.result = str(living)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask892BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
