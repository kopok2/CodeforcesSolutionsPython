class CodeforcesTask237ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.arrivals = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.arrivals.append([int(y) for y in input().split(" ")])

    def process_task(self):
        times = [0] * (24 * 60)
        for arr in self.arrivals:
            times[arr[0] * 60 + arr[1]] += 1
        self.result = str(max(times))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask237ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
