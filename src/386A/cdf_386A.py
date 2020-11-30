from operator import itemgetter


class CodeforcesTask386ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.bids = []

    def read_input(self):
        self.n = int(input())
        self.bids = [int(x) for x in input().split(" ")]

    def process_task(self):
        biding = [(x + 1, self.bids[x]) for x in range(self.n)]
        biding.sort(key=itemgetter(1), reverse=True)
        self.result = "{0} {1}".format(biding[0][0], biding[1][1])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask386ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
