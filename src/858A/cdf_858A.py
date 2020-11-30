import math


def get_lcm(n1, n2):
    # find gcd
    gcd = math.gcd(n1, n2)

    # formula
    result = (n1 * n2) / gcd
    return result


class CodeforcesTask858ASolution:
    def __init__(self):
        self.result = ''
        self.n_k = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.result = str(int(get_lcm(self.n_k[0], 10 ** self.n_k[1])))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask858ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
