class CodeforcesTask104BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.questions = []

    def read_input(self):
        self.n = int(input())
        self.questions = [int(x) for x in input().split(" ")]

    def process_task(self):
        wrong_click_cost = [x for x in range(self.n)]
        cost = 0
        for x in range(self.n):
            cost += 1 + (self.questions[x] - 1) * (1 + wrong_click_cost[x])
        self.result = str(cost)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask104BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
