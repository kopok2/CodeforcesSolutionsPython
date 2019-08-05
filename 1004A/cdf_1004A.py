class CodeforcesTask1004ASolution:
    def __init__(self):
        self.result = ''
        self.n_d = []
        self.locations = []

    def read_input(self):
        self.n_d = [int(x) for x in input().split(" ")]
        self.locations = [int(x) for x in input().split(" ")]

    def process_task(self):
        positions = 2
        locked = []
        for x in range(self.n_d[0] - 1):
            locked.append(self.locations[x + 1] - self.locations[x])
        unlocked = [x for x in locked if x >= self.n_d[1] * 2]
        positions += sum([1 if x == self.n_d[1] * 2 else 2 for x in unlocked])
        self.result = str(positions)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1004ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
