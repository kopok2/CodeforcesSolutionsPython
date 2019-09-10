def e(x, n):
    if x > n:
        return 0
    else:
        return x


class CodeforcesTask644ASolution:
    def __init__(self):
        self.result = ''
        self.n_a_b = []

    def read_input(self):
        self.n_a_b = [int(x) for x in input().split(" ")]

    def process_task(self):
        if self.n_a_b[0] > self.n_a_b[1] * self.n_a_b[2]:
            self.result = "-1"
        else:
            result = []
            for x in range(self.n_a_b[1]):
                row = []
                for y in range(self.n_a_b[2]):
                    row.append(x * self.n_a_b[2] + y + 1)
                result.append(row)
            if not self.n_a_b[2] % 2:
                for x in range(self.n_a_b[1]):
                    if x % 2:
                        result[x] = result[x][::-1]
            printable = [" ".join([str(e(x, self.n_a_b[0])) for x in row]) for row in result]
            self.result = "\n".join(printable)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask644ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
