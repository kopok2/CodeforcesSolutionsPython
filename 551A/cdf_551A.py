from operator import itemgetter


class CodeforcesTask551ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.ranking = []

    def read_input(self):
        self.n = int(input())
        self.ranking = [int(x) for x in input().split(" ")]

    def process_task(self):
        positions = [[x, self.ranking[x], 0] for x in range(self.n)]
        positions.sort(key=itemgetter(1), reverse=True)
        cnt = 0
        pos = 1
        mx = positions[0][1]
        for x in range(self.n):
            if positions[x][1] < mx:
                mx = positions[x][1]
                pos = 1 + cnt
            cnt += 1
            positions[x][2] = pos
        positions.sort(key=itemgetter(0))
        self.result = " ".join([str(x[2]) for x in positions])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask551ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
