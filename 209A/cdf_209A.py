class CodeforcesTask209ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        ways = [0] * (self.n + 1)
        ways[0] = 1
        ways[1] = 2
        md = 1000000007
        for x in range(2, self.n + 1):
            ways[x] = (1 + ways[x - 1] + ways[x - 2]) % md
        #print(ways)
        self.result = str(ways[self.n] - 1)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask209ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
