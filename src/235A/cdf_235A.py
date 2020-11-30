import math


def lcm(n1, n2):
    # find gcd
    gcd = math.gcd(n1, n2)

    # formula
    result = (n1 * n2) / gcd
    return result


class CodeforcesTask235ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        aa = 0
        for x in range(100):
            for y in range(100):
                for z in range(100):
                    a = int(lcm(int(lcm(max(1, self.n - z), max(1, (self.n - x)))), max(1, (self.n - y))))
                    aa = max(aa, a)
        x = int(lcm(int(lcm(self.n, max(1, (self.n - 1)))), max(1, (self.n - 2))))
        y = int(lcm(int(lcm(self.n, max(1, (self.n - 1)))), max(1, (self.n - 3))))
        z = int(lcm(int(lcm(self.n, max(1, (self.n - 2)))), max(1, (self.n - 3))))

        print(x, y, z, aa)
        self.result = str(x)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask235ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
