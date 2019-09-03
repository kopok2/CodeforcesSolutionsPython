import math


def get_lcm(n1, n2):
    # find gcd
    gcd = math.gcd(n1, n2)

    # formula
    result = (n1 * n2) / gcd
    return result


class CodeforcesTask173ASolution:
    def __init__(self):
        self.result = ''
        self.rounds = 0
        self.n_str = ''
        self.p_str = ''

    def read_input(self):
        self.rounds = int(input())
        self.n_str = input()
        self.p_str = input()

    def process_task(self):
        n = int(len(self.n_str))
        k = int(len(self.p_str))
        ap = 0
        bp = 0
        np = 0
        pp = 0
        full_round = int(get_lcm(n, k))
        if self.rounds <= full_round:
            for x in range(self.rounds):
                a = self.n_str[ap]
                b = self.p_str[bp]
                ap += 1
                bp += 1
                if ap >= n:
                    ap = 0
                if bp >= k:
                    bp = 0
                if (a == "R" and b == "S") or (a == "S" and b == "P") or (a == "P" and b == "R"):
                    pp += 1
                elif (b == "R" and a == "S") or (b == "S" and a == "P") or (b == "P" and a == "R"):
                    np += 1
            self.result = "{0} {1}".format(np, pp)
        else:
            for x in range(full_round):
                a = self.n_str[ap]
                b = self.p_str[bp]
                ap += 1
                bp += 1
                if ap >= n:
                    ap = 0
                if bp >= k:
                    bp = 0
                if (a == "R" and b == "S") or (a == "S" and b == "P") or (a == "P" and b == "R"):
                    pp += 1
                elif (b == "R" and a == "S") or (b == "S" and a == "P") or (b == "P" and a == "R"):
                    np += 1
            np *= self.rounds // full_round
            pp *= self.rounds // full_round
            for x in range(self.rounds % full_round):
                a = self.n_str[ap]
                b = self.p_str[bp]
                ap += 1
                bp += 1
                if ap >= n:
                    ap = 0
                if bp >= k:
                    bp = 0
                if (a == "R" and b == "S") or (a == "S" and b == "P") or (a == "P" and b == "R"):
                    pp += 1
                elif (b == "R" and a == "S") or (b == "S" and a == "P") or (b == "P" and a == "R"):
                    np += 1
            self.result = "{0} {1}".format(np, pp)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask173ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
