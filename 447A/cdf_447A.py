def h(x, p):
    return x % p


class CodeforcesTask447ASolution:
    def __init__(self):
        self.result = ''
        self.p_n = []
        self.inserts = []

    def read_input(self):
        self.p_n = [int(x) for x in input().split(" ")]
        self.inserts = [int(input()) for x in range(self.p_n[1])]

    def process_task(self):
        hashes = [False for x in range(self.p_n[0])]
        result = -1
        for i, x in enumerate(self.inserts):
            if hashes[h(x, self.p_n[0])]:
                if result < 0:
                    result = i + 1
            else:
                hashes[h(x, self.p_n[0])] = True
        self.result = str(result)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask447ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
