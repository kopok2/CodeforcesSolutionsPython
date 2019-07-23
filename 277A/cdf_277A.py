class CodeforcesTask277ASolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.langs = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[0]):
            self.langs.append([int(y) for y in input().split(" ")])

    def process_task(self):
        if not sum([x[0] for x in self.langs]):
            self.result = str(self.n_m[0])
        else:
            graph = []
            for i, employee in enumerate(self.langs):
                #               id           conn                             empl visited blockid
                graph.append([i + 1, [x + self.n_m[0] for x in employee[1:]], True, False, 0])
            for x in range(self.n_m[1]):
                graph.append([x + self.n_m[0] +1, [], False, False, 0])
            for i, employee in enumerate(self.langs):
                for x in employee[1:]:
                    graph[x + self.n_m[0] - 1][1].append(i + 1)

            empl_blocks = 0
            blocks = 0
            traversed = 0
            while traversed < len(graph):
                to_visit = []
                for g in graph:
                    if not g[4]:
                        to_visit.append(g[0])
                        break
                blocks += 1
                is_empl_bl = False
                while to_visit:

                    visiting = to_visit.pop(0)
                    if not graph[visiting - 1][4]:
                        traversed += 1
                        graph[visiting - 1][4] = blocks
                        if not is_empl_bl:
                            if graph[visiting - 1][2]:
                                is_empl_bl = True
                                empl_blocks += 1
                        to_visit += [x for x in graph[visiting - 1][1] if graph[x - 1][3] == 0]
            #print(blocks, empl_blocks)
            #for g in graph:
            #    print(g)
            self.result = str(empl_blocks - 1)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask277ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
