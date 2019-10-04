def nxt_num(n):
    return 10 ** len(str(n))


class CodeforcesTask373BSolution:
    def __init__(self):
        self.result = ''
        self.w_m_k = []

    def read_input(self):
        self.w_m_k = [int(x) for x in input().split(" ")]

    def process_task(self):
        k = self.w_m_k[2]
        budget = self.w_m_k[0]
        pos = self.w_m_k[1]
        length = 0
        while True:
            if (nxt_num(pos) - pos) * len(str(pos)) * k <= budget:
                budget -= (nxt_num(pos) - pos) * len(str(pos)) * k
                length += nxt_num(pos) - pos
                pos = nxt_num(pos)
            else:
                fin = budget // (len(str(pos)) * k)
                budget -= fin * (len(str(pos)) * k)
                length += fin
                break
        self.result = str(length)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask373BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
