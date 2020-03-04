class CodeforcesTask632BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.strengths = []
        self.teams = ''

    def read_input(self):
        self.n = int(input())
        self.strengths = [int(x) for x in input().split(" ")]
        self.teams = input()

    def process_task(self):
        a_score = 0
        b_score = 0
        for x in range(self.n):
            if self.teams[x] == "A":
                a_score += self.strengths[x]
            else:
                b_score += self.strengths[x]
        mx_chng = 0
        res = 0
        resback = 0
        for for_mv in range(self.n):
            if self.teams[for_mv] == "A":
                res += self.strengths[for_mv]
            else:
                res -= self.strengths[for_mv]
            mx_chng = max(mx_chng, res)
        for back_mv in range(self.n - 1, 0, -1):
            if self.teams[back_mv] == "A":
                resback += self.strengths[back_mv]
            else:
                resback -= self.strengths[back_mv]
            mx_chng = max(mx_chng, resback)
        self.result = str(mx_chng + b_score)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask632BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
