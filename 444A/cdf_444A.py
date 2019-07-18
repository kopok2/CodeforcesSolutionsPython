def dense(e, v):
    if e:
        return v / e
    else:
        return 0


def sub_value(nodes, tree, egdes):
    v = 0
    for eg in nodes:
        v += tree[eg - 1][1]
    e = 0
    for eg in egdes:
        if eg[0] in nodes and eg[1] in nodes:
            e += eg[2]
    return dense(e, v)


class CodeforcesTask444ASolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.nodes = []
        self.edges = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        self.nodes = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[1]):
            self.edges.append([int(x) for x in input().split(" ")])

    def process_task(self):
        #print(self.nodes)
        #print(self.edges)
        graph = [[i + 1, x, []] for i, x in enumerate(self.nodes)]
        for e in self.edges:
            graph[e[0] - 1][2].append(e[1])
            graph[e[1] - 1][2].append(e[0])
        maxed = 0
        in_g = []
        for starting in graph:
            if not starting[0] in in_g:
                in_g = [starting[0]]
                to_visit = starting[2]
                result = 0
                while to_visit:
                    visiting = to_visit.pop(0)
                    newset = in_g + [visiting]
                    nw = sub_value(newset, graph, self.edges)
                    if nw > result:
                        result = nw
                        in_g = newset
                        to_visit += [x for x in graph[visiting - 1][2] if x not in in_g]
                        if result > maxed:
                            maxed = result

        self.result = str(maxed)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask444ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
