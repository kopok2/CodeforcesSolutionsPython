class CodeforcesTask796ASolution:
    def __init__(self):
        self.result = ''
        self.n_m_k = []
        self.prices = []

    def read_input(self):
        self.n_m_k = [int(x) for x in input().split(" ")]
        self.prices = [int(x) for x in input().split(" ")]

    def process_task(self):
        left = self.prices[:self.n_m_k[1] - 1][::-1]
        right = self.prices[self.n_m_k[1]:]
        dl = 1000
        dr = 1000
        i = 1
        for l in left:
            if l:
                if l <= self.n_m_k[2]:
                    dl = i
                    break
            i += 1
        i = 1
        for l in right:
            if l:
                if l <= self.n_m_k[2]:
                    dr = i
                    break
            i += 1
        dist = 10 * min(dl, dr)
        self.result = str(dist)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask796ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
