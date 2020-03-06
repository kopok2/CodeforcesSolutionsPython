def f(p, k):
    res = []
    for r in range(len(p) // k):
        new = p[:k]
        #print(k, new)
        res += new[1:]
        res.append(new[0])
        p = p[k:]
    if p:
        res += p[1:]
        res.append(p[0])
    return res



class CodeforcesTask286BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        p = list(range(1, self.n + 1))
        for k in range(2, self.n + 1):
            p = f(p, k)
        self.result = " ".join([str(x) for x in p])


    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask286BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
