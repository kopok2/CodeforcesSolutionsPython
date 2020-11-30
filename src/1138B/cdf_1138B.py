from operator import itemgetter


class CodeforcesTask1138BSolution:
    def __init__(self):
        self.result = ''
        self.artist_count = 0
        self.clowns = []
        self.acrobats = []

    def read_input(self):
        self.artist_count = int(input())
        self.clowns = [int(x) for x in input()]
        self.acrobats = [int(x) for x in input()]

    def process_task(self):
        pure_clowns = 0
        pure_acrobats = 0
        pure_useless = 0
        pure_both = 0
        for x in range(self.artist_count):
            if self.acrobats[x]:
                if self.clowns[x]:
                    pure_both += 1
                else:
                    pure_acrobats += 1
            else:
                if self.clowns[x]:
                    pure_clowns += 1
                else:
                    pure_useless += 1
        #print(pure_useless, pure_acrobats, pure_clowns, pure_both)
        eq = self.artist_count // 2 - pure_acrobats - pure_both
        a_d = []
        possible_a = [x for x in range(pure_useless + 1)]
        for pos_a in possible_a:
            d = pos_a - eq
            if d <= pure_both and d >= 0:
                a_d.append((pos_a, d))
        #print(a_d, eq)
        possb = [x for x in range(pure_acrobats + 1)]
        possc = [x for x in range(pure_clowns + 1)]
        solutions = []
        for para in a_d:
            eq2 = pure_acrobats + pure_both - 2 * para[1]
            for b in possb:
                c = eq2 - b
                if c in possc:
                    solutions.append([para[0], b, c, para[1]])
                    break
            if solutions:
                break
        if not solutions:
            self.result = "-1"
        else:
            squad = []
            for x in range(self.artist_count):
                if self.acrobats[x]:
                    if self.clowns[x]:
                        if solutions[0][3]:
                            solutions[0][3] -= 1
                            squad.append(x)
                    else:
                        if solutions[0][1]:
                            solutions[0][1] -= 1
                            squad.append(x)
                else:
                    if self.clowns[x]:
                        if solutions[0][2]:
                            solutions[0][2] -= 1
                            squad.append(x)
                    else:
                        if solutions[0][0]:
                            solutions[0][0] -= 1
                            squad.append(x)
            self.result = " ".join([str(x+1) for x in squad])
        #print(solutions)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1138BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
