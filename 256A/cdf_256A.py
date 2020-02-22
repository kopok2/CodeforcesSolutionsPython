class CodeforcesTask256ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.sequence = []

    def read_input(self):
        self.n = int(input())
        self.sequence = [int(x) for x in input().split(" ")]

    def process_task(self):
        mx_len = 1
        for start in range(self.n - 1):
            a1 = self.sequence[start]
            # a2 = a1 + (-1)^1 + 1q = a1 - q
            # q = a1 - a2
            for second in range(start + 1, self.n):
                a2 = self.sequence[second]
                q = a1 - a2
                cr_l = 2
                pos = second + 1
                mx_len = max(mx_len, cr_l)
                last = a2
                while pos < self.n:
                    nxt =
                    if self.sequence[pos] == last + ((-1) ** (cr_l + 2)) * q:
                        cr_l += 1
                        last += ((-1) ** (cr_l + 1)) * q
                        mx_len = max(mx_len, cr_l)
                    pos += 1
        self.result = str(mx_len)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask256ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
