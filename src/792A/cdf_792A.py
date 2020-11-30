class CodeforcesTask792ASolution:
    def __init__(self):
        self.result = ''
        self.cities = 0
        self.cords = []

    def read_input(self):
        self.cities = int(input())
        self.cords = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.cords.sort()
        dists = [self.cords[x + 1] - self.cords[x] for x in range(self.cities - 1)]
        smallest_dist = min(dists)
        sm_dist_quant = dists.count(smallest_dist)
        self.result = "{0} {1}".format(smallest_dist, sm_dist_quant)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask792ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
