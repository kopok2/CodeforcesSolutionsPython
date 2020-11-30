class CodeforcesTask285BSolution:
    def __init__(self):
        self.result = ''
        self.n_s_t = []
        self.p = []

    def read_input(self):
        self.n_s_t = [int(x) for x in input().split(" ")]
        self.p = [int(x) for x in input().split(" ")]

    def process_task(self):
        n, s, t = self.n_s_t
        if s == t:
            self.result = "0"
        else:
            connected = True
            pos = s
            steps = 0
            while pos != t:
                steps += 1
                pos = self.p[pos - 1]
                if steps > n:
                    connected = False
                    break
            if not connected:
                self.result = "-1"
            else:
                self.result = str(steps)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask285BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
