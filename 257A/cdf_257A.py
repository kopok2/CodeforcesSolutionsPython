class CodeforcesTask257ASolution:
    def __init__(self):
        self.result = ''
        self.n_m_k = []
        self.filters =[]

    def read_input(self):
        self.n_m_k = [int(x) for x in input().split(" ")]
        self.filters = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.filters.sort(reverse=True)
        needed = 0
        if self.n_m_k[1] - self.n_m_k[2]:
            undirect = self.n_m_k[1] + 1 - self.n_m_k[2]
        else:
            undirect = 0
        #print(self.filters, undirect)
        if undirect > 0:
            undirect -= 1
            for supply_filter in self.filters:
                #print(needed, undirect)
                needed += 1
                undirect -= supply_filter - 1
                if undirect <= 0:
                    break
        if undirect > 0:
            self.result = "-1"
        else:
            self.result = str(needed)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask257ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
