from collections import defaultdict


class CodeforcesTask551BSolution:
    def __init__(self):
        self.result = ''
        self.a = ''
        self.b = ''
        self.c = ''

    def read_input(self):
        self.a = input()
        self.b = input()
        self.c = input()

    def process_task(self):
        to_be_used = defaultdict(int)
        for a in self.a:
            to_be_used[a] += 1
        b_d = defaultdict(int)
        c_d = defaultdict(int)

        for a in self.b:
            b_d[a] += 1

        for a in self.c:
            c_d[a] += 1

        mx = 0
        mx_sol = [0, 0]
        mnb = min([to_be_used[x] // b_d[x] for x in b_d.keys()])
        for b in range(mnb + 1):
            for a in b_d.keys():
                to_be_used[a] -= b_d[a] * b
            mnc = min([to_be_used[x] // c_d[x] for x in c_d.keys()])
            if mnc + b > mx:
                mx = mnc + b
                mx_sol = [b, mnc]
            for a in b_d.keys():
                to_be_used[a] += b_d[a] * b
        for a in b_d.keys():
            to_be_used[a] -= b_d[a] * mx_sol[0]
        for a in c_d.keys():
            to_be_used[a] -= c_d[a] * mx_sol[1]
        self.result = mx_sol[0] * self.b + mx_sol[1] * self.c
        for r in to_be_used.keys():
            if to_be_used[r]:
                self.result += r * to_be_used[r]

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask551BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
