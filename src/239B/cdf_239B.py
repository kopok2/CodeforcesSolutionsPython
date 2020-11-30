class CodeforcesTask239BSolution:
    def __init__(self):
        self.result = ''
        self.n_q = []
        self.program = []
        self.queries = []

    def read_input(self):
        self.n_q = [int(x) for x in input().split(" ")]
        self.program = list(input())
        for x in range(self.n_q[1]):
            self.queries.append([int(y) for y in input().split(" ")])

    def process_task(self):
        program = [int(x) if x in "0123456789" else x for x in self.program]
        for query in self.queries:
            counts = [0 for x in range(10)]
            going_right = True
            routine = program[query[0] - 1:query[1]]
            cp = 0
            changed = False
            while 0 <= cp < len(routine):
                #print(routine, cp, going_right)
                if routine[cp] == ">":

                    if changed:
                        if going_right:
                            del routine[cp - 1]
                            cp -= 1
                        else:
                            del routine[cp + 1]
                    else:
                        changed = True
                    going_right = True
                elif routine[cp] == "<":

                    if changed:
                        if going_right:
                            del routine[cp - 1]
                            cp -= 1
                        else:
                            del routine[cp + 1]
                    else:
                        changed = True
                    going_right = False
                else:
                    changed = False
                    counts[routine[cp]] += 1
                    if routine[cp] > 0:
                        routine[cp] -= 1
                    else:
                        del routine[cp]
                        cp -= 1
                if going_right:
                    cp += 1
                else:
                    cp -= 1
            self.result += "{0}\n".format(" ".join([str(x) for x in counts]))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask239BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
