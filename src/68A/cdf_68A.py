from itertools import permutations


class CodeforcesTask68ASolution:
    def __init__(self):
        self.result = ''
        self.pppp_a_b = []

    def read_input(self):
        self.pppp_a_b = [int(x) for x in input().split(" ")]

    def process_task(self):
        prop = [0] * (1 + self.pppp_a_b[-1] - self.pppp_a_b[-2])
        for st in permutations(self.pppp_a_b[:4]):
            f = lambda x: (((x % st[0]) % st[1]) % st[2]) % st[3]
            for y in range(self.pppp_a_b[-2], self.pppp_a_b[-1] + 1):
                if f(y) == y:
                    prop[y - self.pppp_a_b[-2]] += 1
        has_prop = [1 if x >= 7 else 0 for x in prop]
        self.result = str(sum(has_prop))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask68ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
