class CodeforcesTask347BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.permutation = []

    def read_input(self):
        self.n = int(input())
        self.permutation = [int(x) for x in input().split(" ")]

    def process_task(self):
        fixed_points = sum([1 if self.permutation[x] == x else 0 for x in range(self.n)])
        if fixed_points == self.n:
            self.result = str(self.n)
        else:
            double = False
            for x in range(self.n):
                if self.permutation[x] != x:
                    if self.permutation[self.permutation[x]] == x:
                        double = True
                        break
            if double:
                fixed_points += 2
            else:
                fixed_points += 1
            self.result = str(fixed_points)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask347BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
