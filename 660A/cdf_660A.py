import math


class CodeforcesTask660ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.array = []

    def read_input(self):
        self.n = int(input())
        self.array = [int(x) for x in input().split(" ")]

    def process_task(self):
        coprimism = [1 if math.gcd(self.array[x - 1], self.array[x]) == 1.0 else 0 for x in range(1, self.n)]
        k = self.n - sum(coprimism) - 1
        new_array = [self.array[0]]
        for x in range(1, self.n):
            if not coprimism[x - 1]:
                new_array.append(1)
            new_array.append(self.array[x])
        self.result = "{0}\n{1}".format(k, " ".join([str(x) for x in new_array]))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask660ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
