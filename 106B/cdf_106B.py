from operator import itemgetter


class CodeforcesTask106BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.laptops = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.laptops.append([x + 1] + [int(y) for y in input().split(" ")] + [False])

    def process_task(self):
        for laptop in self.laptops:
            for other in self.laptops:
                if laptop != other:
                    if other[1] < laptop[1] and other[2] < laptop[2] and other[3] < laptop[3]:
                        other[5] = True
        self.laptops = [x for x in self.laptops if not x[5]]
        self.laptops.sort(key=itemgetter(4))
        self.result = str(self.laptops[0][0])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask106BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
