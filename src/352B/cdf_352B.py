from operator import itemgetter


def is_prog(seq):
    if len(seq) == 1:
        return True
    else:
        d = seq[1] - seq[0]
        is_ = True
        s1 = seq[0]
        for x in range(len(seq)):
            if seq[x] != s1 + d * x:
                is_ = False
                break
        return is_


class CodeforcesTask352BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.sequence = []

    def read_input(self):
        self.n = int(input())
        self.sequence = [int(x) for x in input().split(" ")]

    def process_task(self):
        xs = {}
        for x in range(1, self.n + 1):
            if self.sequence[x - 1] in xs:
                xs[self.sequence[x - 1]].append(x)
            else:
                xs[self.sequence[x - 1]] = [x]
        result = []
        for key, value in xs.items():
            value.sort()
            if is_prog(value):
                if len(value) > 1:
                    d = value[1] - value[0]
                else:
                    d = 0
                result.append((key, d))
        result.sort(key=itemgetter(0))
        self.result = "{0}\n{1}".format(len(result), "\n".join([" ".join([str(r) for r in x]) for x in result]))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask352BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
