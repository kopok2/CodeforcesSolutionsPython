class CodeforcesTask214BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.digits = []

    def read_input(self):
        self.n = int(input())
        self.digits = [int(x) for x in input().split(" ")]

    def process_task(self):
        digits_cnt = [0] * 10
        for x in self.digits:
            digits_cnt[x] += 1
        if not digits_cnt[0]:
            self.result = "-1"
        else:
            ss = sum([x * digits_cnt[x] for x in range(10)])
            if ss % 3 == 0:
                for x in range(10):
                    self.result += str(x) * digits_cnt[x]
                self.result = self.result[::-1]
            elif ss % 3 == 1:
                if digits_cnt[1]:
                    digits_cnt[1] -= 1
                elif digits_cnt[4]:
                    digits_cnt[4] -= 1
                elif digits_cnt[7]:
                    digits_cnt[7] -= 1
                for x in range(10):
                    self.result += str(x) * digits_cnt[x]
                self.result = self.result[::-1]
            elif ss % 3 == 2:
                if digits_cnt[2]:
                    digits_cnt[2] -= 1
                elif digits_cnt[5]:
                    digits_cnt[5] -= 1
                elif digits_cnt[8]:
                    digits_cnt[8] -= 1
                for x in range(10):
                    self.result += str(x) * digits_cnt[x]
                self.result = self.result[::-1]


    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask214BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
