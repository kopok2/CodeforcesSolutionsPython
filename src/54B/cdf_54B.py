def rotate(puzzle):
    n_puzzle = []
    for y in range(len(puzzle) - 1, -1, -1):
        n_puzzle.append(puzzle[y])
    result = []
    for x in range(len(puzzle[0])):
        col = []
        for y in range(len(puzzle)):
            col.append(n_puzzle[y][x])
        result.append(col)
    return result


def puzzle_match(p1, p2):
    r1 = p2
    r2 = rotate(p2)
    r3 = rotate(r2)
    r4 = rotate(r3)
    variants = [r1, r2, r3, r4]
    return p1 in variants


def make_puzzles(puzzle, x_cuts, y_cuts, a, b):
    x_size = a // x_cuts
    y_size = b // y_cuts
    result = []
    for x in range(x_cuts):
        for y in range(y_cuts):
            p = []
            for i in range(x_size):
                row = []
                for j in range(y_size):
                    row.append(puzzle[x * x_size + i][y * y_size + j])
                p.append(row)
            result.append(p)
    return result


class CodeforcesTask54BSolution:
    def __init__(self):
        self.result = ''
        self.a_b = []
        self.puzzle = []

    def read_input(self):
        self.a_b = [int(x) for x in input().split(" ")]
        for x in range(self.a_b[0]):
            self.puzzle.append(list(input()))

    def process_task(self):
        x_cuts = [x for x in range(1, self.a_b[0] + 1) if not self.a_b[0] % x][::-1]
        y_cuts = [x for x in range(1, self.a_b[1] + 1) if not self.a_b[1] % x][::-1]
        variants = 0
        varianted = []
        for x in x_cuts:
            for y in y_cuts:
                puzzles = make_puzzles(self.puzzle, x, y, self.a_b[0], self.a_b[1])
                rotated = []
                valid = True
                for p in puzzles:
                    r1 = p
                    r2 = rotate(r1)
                    r3 = rotate(r2)
                    r4 = rotate(r3)
                    for r in (r1, r2, r3, r4):
                        if r in rotated:
                            valid = False
                            break
                    if not valid:
                        break
                    rotated += [r1, r2, r3, r4]
                if valid:
                    variants += 1
                    varianted.append((self.a_b[0] // x, self.a_b[1] // y))
        varianted.sort(key=lambda x: x[0]*x[1])
        self.result = "{0}\n{1} {2}".format(variants, varianted[0][0], varianted[0][1])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask54BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
