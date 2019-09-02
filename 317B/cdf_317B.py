class CodeforcesTask317BSolution:
    def __init__(self):
        self.result = ''
        self.n_t = []
        self.queries = []

    def read_input(self):
        self.n_t = [int(x) for x in input().split(" ")]
        for x in range(self.n_t[1]):
            self.queries.append([int(y) for y in input().split(" ")])

    def process_task(self):
        ant_map = {"0_0": self.n_t[0]}
        moved = True
        while moved:
            moved = False
            new_map = {}
            for cord, ants in ant_map.items():
                if ants >= 4:
                    x, y = [int(z) for z in cord.split("_")]
                    down = "{0}_{1}".format(x + 1, y)
                    right = "{0}_{1}".format(x, y + 1)
                    left = "{0}_{1}".format(x, y - 1)
                    up = "{0}_{1}".format(x - 1, y)
                    if cord in new_map:
                        new_map[cord] += ants - 4
                    else:
                        new_map[cord] = ants - 4
                    if down in new_map:
                        new_map[down] += 1
                    else:
                        new_map[down] = 1
                    if right in new_map:
                        new_map[right] += 1
                    else:
                        new_map[right] = 1
                    if left in new_map:
                        new_map[left] += 1
                    else:
                        new_map[left] = 1
                    if up in new_map:
                        new_map[up] += 1
                    else:
                        new_map[up] = 1
                    moved = True
                else:
                    if cord in new_map:
                        new_map[cord] += ants
                    else:
                        new_map[cord] = ants
            ant_map = new_map
        results = []
        for query in self.queries:
            q_cord = "{0}_{1}".format(*query)
            if q_cord in ant_map:
                results.append(ant_map[q_cord])
            else:
                results.append(0)
        self.result = "\n".join([str(x) for x in results])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask317BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
