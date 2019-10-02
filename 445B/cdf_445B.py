class CodeforcesTask445BSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.reactions = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[1]):
            self.reactions.append([int(y) for y in input().split(" ")])

    def process_task(self):
        reactions_cnt = 0
        danger = 1
        reaction_groups = {}
        graph = [[[], -1] for x in range(self.n_m[0])]
        for react in self.reactions:
            graph[react[0] - 1][0].append(react[1])
            graph[react[1] - 1][0].append(react[0])
        starts = [x + 1 for x in range(self.n_m[0])]
        while starts:
            starting = starts.pop(-1)
            if graph[starting - 1][1] == -1:
                reactions_cnt += 1
                reaction_groups[reactions_cnt] = 1
                graph[starting - 1][1] = reactions_cnt
                to_visit = graph[starting - 1][0]
                while to_visit:
                    visiting = to_visit.pop(-1)
                    if graph[visiting - 1][1] == -1:
                        graph[visiting - 1][1] = reactions_cnt
                        reaction_groups[reactions_cnt] += 1
                        to_visit += graph[visiting - 1][0]
        for key, val in reaction_groups.items():
            danger *= 2 ** (val - 1)
        self.result = str(danger)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask445BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
