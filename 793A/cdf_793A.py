class CodeforcesTask793ASolution:
    def __init__(self):
        self.result = ''
        self.n_k = []
        self.shares = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]
        self.shares = [int(x) for x in input().split(" ")]

    def process_task(self):
        rests = [x % self.n_k[1] for x in self.shares]
        if len(set(rests)) > 1:
            self.result = "-1"
        else:
            adj_shares = [(x - rests[0]) // self.n_k[1] for x in self.shares]
            base_share = min(adj_shares)
            times = [x - base_share for x in adj_shares]
            self.result = str(sum(times))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask793ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
