class CodeforcesTask602BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.sequence = []

    def read_input(self):
        self.n = int(input())
        self.sequence = [int(x) for x in input().split(" ")]

    def process_task(self):
        devel = [x % 3 for x in self.sequence]
        maxlen = 0
        for level in range(3):
            clen = 0
            for x in range(self.n):
                if devel[x] == level:
                    maxlen = max(maxlen, clen)
                    clen = 0
                else:
                    clen += 1
            maxlen = max(maxlen, clen)
        self.result = str(maxlen)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask602BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
