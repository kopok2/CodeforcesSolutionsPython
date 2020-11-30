from operator import itemgetter


class CodeforcesTask31ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.lens = []

    def read_input(self):
        self.n = int(input())
        self.lens = [int(x) for x in input().split(" ")]

    def process_task(self):
        result = []
        got = False
        for x in range(self.n):
            for y in range(self.n):
                for z in range(self.n):
                    if len({x, y, z}) == 3:
                        a, b, c = self.lens[x], self.lens[y], self.lens[z]
                        ss = a + b + c
                        if not ss % 2:
                            if ss // 2 in {a, b, c}:
                                result = [(a, x), (b, y), (c, z)]
                                result.sort(key=itemgetter(0), reverse=True)
                                got = True
                    if got:
                        break
                if got:
                    break
            if got:
                break

        self.result = "-1" if not result else " ".join([str(x[1] + 1) for x in result])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask31ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
