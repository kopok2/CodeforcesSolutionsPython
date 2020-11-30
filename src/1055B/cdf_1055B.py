class CodeforcesTask1055BSolution:
    def __init__(self):
        self.result = ''
        self.n_m_l = []
        self.hairline = []
        self.queries = []

    def read_input(self):
        self.n_m_l = [int(x) for x in input().split(" ")]
        self.hairline = [int(x) for x in input().split(" ")]
        for _ in range(self.n_m_l[1]):
            self.queries.append([int(y) for y in input().split(" ")])

    def process_task(self):
        res = []
        time = 0
        comp = [0] * self.n_m_l[0]
        add = [[1, x + 1, self.hairline[x]] for x in range(self.n_m_l[0])]
        self.queries = add + self.queries
        self.hairline = [0] * self.n_m_l[0]
        for q in self.queries:
            if not q[0]:
                res.append(time)
            else:
                if self.hairline[q[1] - 1] <= self.n_m_l[2] < self.hairline[q[1] - 1] + q[2]:
                    comp[q[1] - 1] = 1
                    if self.n_m_l[0] > 1:
                        if 1 < q[1] < self.n_m_l[0]:
                            if comp[q[1] - 2] and comp[q[1]]:
                                time -= 1
                            elif not comp[q[1] - 2] and not comp[q[1]]:
                                time += 1
                        elif q[1] == 1:
                            if not comp[1]:
                                time += 1
                        elif q[1] == self.n_m_l[0]:
                            if not comp[-2]:
                                time += 1
                    else:
                        time += 1
                self.hairline[q[1] - 1] += q[2]
        self.result = "\n".join([str(x) for x in res])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1055BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
