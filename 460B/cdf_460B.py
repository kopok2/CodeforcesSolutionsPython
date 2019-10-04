class CodeforcesTask460BSolution:
    def __init__(self):
        self.result = ''
        self.a_b_c = []

    def read_input(self):
        self.a_b_c = [int(x) for x in input().split(" ")]

    def process_task(self):
        solutions = set()
        for y in range(1, 100):
            sol = self.a_b_c[1] * (y ** self.a_b_c[0]) + self.a_b_c[2]
            if 0 < sol <= 10 ** 9 + 1:
                if sum([int(x) for x in str(sol)]) == y:
                    solutions.add(sol)
        solutions = sorted(list(solutions))
        self.result = "{0}\n{1}".format(len(solutions), " ".join([str(x) for x in solutions]))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask460BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
