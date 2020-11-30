import math
from functools import reduce


def factors(n):
    return list(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


class CodeforcesTask154BSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.commands = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[1]):
            self.commands.append(int(input().replace(" ", "")))

    def process_task(self):
        states = [False] * self.n_m[0]
        constraints = [[] for _ in range(self.n_m[0])]
        on = set()
        result = []
        for q in self.commands:
           if q > 0:
                if not states[q - 1]:
                    res = True
                    if constraints[q - 1]:
                        res = False
                        conf = constraints[q - 1][0]
                    if res:
                        on.add(q)
                        states[q - 1] = True
                        result.append("Success")
                    else:
                        result.append(f"Conflict with {conf}")
                else:
                    result.append("Already on")
           else:
                if states[-q - 1]:
                    states[-q - 1] = False
                    on.remove(-q)
                    result.append("Success")
                else:
                    result.append("Already off")
        self.result = "\n".join(result)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask154BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
