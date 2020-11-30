class CodeforcesTask268ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.teams = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.teams.append([int(y) for y in input().split(" ")])

    def process_task(self):
        hosts = [x[0] for x in self.teams]
        guests = [x[1] for x in self.teams]
        times = 0
        for ho in hosts:
            times += guests.count(ho)
        self.result = str(times)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask268ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
