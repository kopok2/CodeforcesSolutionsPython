class CodeforcesTask1043ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.votes = []

    def read_input(self):
        self.n = int(input())
        self.votes = [int(x) for x in input().split(" ")]

    def process_task(self):
        k = max(self.votes)
        while k * self.n - sum(self.votes) <= sum(self.votes):
            k += 1
        self.result = str(max(max(self.votes), k))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1043ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
