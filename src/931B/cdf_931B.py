import math


class CodeforcesTask931BSolution:
    def __init__(self):
        self.result = ''
        self.n_a_b = []

    def read_input(self):
        self.n_a_b = [int(x) for x in input().split(" ")]

    def process_task(self):
        result = 0
        table = [x + 1 for x in range(self.n_a_b[0])]
        for r in range(int(math.log2(self.n_a_b[0]))):
            ntable = [0 for x in range(self.n_a_b[0] // 2 ** (r + 1))]
            for x in range(len(table) // 2):
                winner = table[x * 2]
                if table[x * 2 + 1] in self.n_a_b[1:]:
                    if winner in self.n_a_b[1:]:
                        result = r + 1
                    else:
                        winner = table[x * 2 + 1]
                ntable[x] = winner
            table = ntable
        if result == int(math.log2(self.n_a_b[0])):
            self.result = "Final!"
        else:
            self.result = str(result)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask931BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
