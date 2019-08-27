class CodeforcesTask890BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.cafes = []

    def read_input(self):
        self.n = int(input())
        self.cafes = [int(x) for x in input().split(" ")]

    def process_task(self):
        last_visit = [-1 for x in range(200_001)]
        for x in range(self.n):
            last_visit[self.cafes[x]] = x + 1
        earliest = -1
        earliest_time = -1
        for x in range(200_001):
            if last_visit[x] > 0:
                if earliest_time < 0:
                    earliest_time = last_visit[x] + 1
                    earliest = x
                elif earliest_time > last_visit[x] + 1:
                    earliest_time = last_visit[x] + 1
                    earliest = x
        self.result = str(earliest)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask890BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
