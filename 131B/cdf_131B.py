class CodeforcesTask131BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.clients = []

    def read_input(self):
        self.n = int(input())
        self.clients = [int(x) for x in input().split(" ")]

    def process_task(self):
        matches = {}
        for c in self.clients:
            if c in matches:
                matches[c] += 1
            else:
                matches[c] = 1
        match_cnt = 0
        for x in set([y for y in self.clients if y > 0]):
            if x in matches and -x in matches:
                match_cnt += matches[x] * matches[-x]
        if 0 in matches:
            if matches[0] > 1:
                match_cnt += (matches[0] * (matches[0] - 1)) // 2
        self.result = str(match_cnt)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask131BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
