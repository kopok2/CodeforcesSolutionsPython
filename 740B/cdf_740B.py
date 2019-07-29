class CodeforcesTask740BSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.moods = []
        self.subarrays = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        self.moods = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[1]):
            self.subarrays.append([int(x) for x in input().split(" ")])

    def process_task(self):
        indices = [self.moods[x[0] - 1:x[1]] for x in self.subarrays]
        boosts = [sum(x) for x in indices]
        mood = sum([x for x in boosts if x > 0])
        self.result = str(mood)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask740BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
