class CodeforcesTask506ASolution:
    def __init__(self):
        self.result = ''
        self.n_d = []
        self.locations = []

    def read_input(self):
        self.n_d = [int(x) for x in input().split(" ")]
        for x in range(self.n_d[0]):
            self.locations.append(int(input()))

    def process_task(self):
        gems = [0] * 30000
        for l in self.locations:
            gems[l - 1] += 1
        dp = gems[::]
        jumps = [set() for x in range(30000)]
        d = max(1, self.n_d[1] - 1)
        jumps[self.n_d[1] - 1] = {d, self.n_d[1], self.n_d[1] + 1}
        for x in range(self.n_d[1] - 1, 30000):
            #print(x, jumps[x])
            for jump in list(jumps[x]):
                #print(jump)
                if x + jump < 30000:
                    #print(x, x + jump)
                    dp[x + jump] = max(dp[x + jump], dp[x] + gems[x + jump])
                    if jump - 1 and x + jump * 2 - 1 < 30000:
                        jumps[x + jump].add(jump - 1)
                    if x + jump * 2 < 30000:
                        jumps[x + jump].add(jump)
                    if x + jump * 2 + 1 < 30000:
                        jumps[x + jump].add(jump + 1)
        self.result = str(max(dp[self.n_d[1] - 1:]))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask506ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
