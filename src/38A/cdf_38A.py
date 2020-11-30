class CodeforcesTask38ASolution:
    def __init__(self):
        self.result = ''
        self.rank_cost = []
        self.rank_desire = []

    def read_input(self):
        input()
        self.rank_cost = [int(x) for x in input().split(" ")]
        self.rank_desire = [int(x) for x in input().split(" ")]

    def process_task(self):
        cost = 0
        for x in range(self.rank_desire[0] - 1, self.rank_desire[1] - 1):
            cost += self.rank_cost[x]
        self.result = str(cost)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask38ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
