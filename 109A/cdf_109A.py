from operator import itemgetter


class CodeforcesTask109ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        pairs = []
        for b in range(self.n // 7 + 1):
            a = (self.n - b * 7) / 4
            if a.is_integer():
                pairs.append((int(a), b, int(a) + b))
        pairs.sort(key=itemgetter(2))
        pairs = [pair for pair in pairs if pair[2] == pairs[0][2]]
        if pairs:
            self.result = "4" * pairs[0][0] + "7" * pairs[0][1]
        else:
            self.result = "-1"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask109ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
