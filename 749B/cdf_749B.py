def dist_sq(p, q):
    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2


class CodeforcesTask749BSolution:
    def __init__(self):
        self.result = ''
        self.points = []

    def read_input(self):
        for x in range(3):
            self.points.append(tuple([int(x) for x in input().split(" ")]))

    def process_task(self):
        selected = []

        self.result = "{0}\n{1}".format(len(selected), "\n".join([" ".join([str(y) for y in p]) for p in selected]))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask749BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
