from collections import deque


class CodeforcesTask964BSolution:
    def __init__(self):
        self.result = ''
        self.n_a_b_c_t = []
        self.times = []

    def read_input(self):
        self.n_a_b_c_t = [int(x) for x in input().split(" ")]
        self.times = [int(x) for x in input().split(" ")]

    def process_task(self):
        rec = [0] * self.n_a_b_c_t[4]
        for t in self.times:
            rec[t - 1] += 1
        bank = 0
        unread = deque()
        for moment in range(self.n_a_b_c_t[4]):
            unread.append([rec[moment], self.n_a_b_c_t[1]])
            for x in range(len(unread)):
                dec = unread.popleft()
                now_cost = dec[0] * dec[1]
                later_cost = dec[0] * (dec[1] - self.n_a_b_c_t[2]) + dec[0] * self.n_a_b_c_t[3]
                if now_cost >= later_cost or moment == self.n_a_b_c_t[4] - 1:
                    bank += now_cost
                else:
                    bank += dec[0] * self.n_a_b_c_t[3]
                    dec[1] -= self.n_a_b_c_t[2]
                    unread.append(dec)
        self.result = str(bank)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask964BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
