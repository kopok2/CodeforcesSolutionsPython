class CodeforcesTask435ASolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.groups = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        self.groups = [int(x) for x in input().split(" ")]

    def process_task(self):
        buses = 1
        bus = 0
        while self.groups:
            if bus + self.groups[0] <= self.n_m[1]:
                bus += self.groups[0]
                self.groups = self.groups[1:]
            else:
                bus = 0
                buses += 1
        self.result = str(buses)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask435ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
