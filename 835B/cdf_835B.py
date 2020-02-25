from collections import Counter
import math


class CodeforcesTask835BSolution:
    def __init__(self):
        self.result = ''
        self.k = 0
        self.n = 0

    def read_input(self):
        self.k = int(input())
        self.n = input()

    def process_task(self):
        digits = [int(x) for x in self.n]
        real_k = sum(digits)
        cnt = Counter(digits)
        if real_k >= self.k:
            self.result = "0"
        else:
            lvl = 0
            diff = 0
            while real_k < self.k:
                # print(lvl, self.k, real_k)
                df_lvl = 9 - lvl
                if cnt[lvl] * df_lvl >= self.k - real_k:
                    diff += math.ceil((self.k - real_k) / df_lvl)
                    real_k = self.k
                    # print((self.k - real_k) / df_lvl, self.k, real_k)
                else:
                    diff += cnt[lvl]
                    real_k += cnt[lvl] * df_lvl
                lvl += 1
            self.result = str(diff)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask835BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
