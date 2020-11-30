class CodeforcesTask386BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.times = []
        self.t = 0

    def read_input(self):
        self.n = int(input())
        self.times = [int(x) for x in input().split(" ")]
        self.t = int(input())

    def process_task(self):
        result = 0

        self.times.sort()

        for start in set(self.times):
            in_range = 0
            for time in self.times:
                if start <= time <= start + self.t:
                    in_range += 1
            result = max(result, in_range)

        self.result = str(result)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask386BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
