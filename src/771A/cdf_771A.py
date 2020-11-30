class CodeforcesTask771ASolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.edges = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[1]):
            self.edges.append([int(y) for y in input().split(" ")])

    def process_task(self):
        graph = [[] for x in range(self.n_m[0])]
        lens = [0] * self.n_m[0]
        for edge in self.edges:
            graph[edge[0] - 1].append(edge[1])
            graph[edge[1] - 1].append(edge[0])
            lens[edge[0] - 1] += 1
            lens[edge[1] - 1] += 1
        component = [0] * self.n_m[0]
        comp_cnt = 0
        can = True
        fixed = set()
        for x in range(self.n_m[0]):
            if not component[x] or self.n_m[0] < 1000:
                if not component[x]:
                    comp_cnt += 1
                    component[x] = comp_cnt
                #print(component, x, graph[x], comp_cnt)
                for y in graph[x]:
                    if lens[y - 1] != lens[x]:
                        #print("x")
                        can = False
                        break
                    elif component[y - 1]:
                        if component[y - 1] != component[x]:
                            #print("d", component)
                            can = False
                            break
                    else:
                        if comp_cnt in fixed:
                            can = False
                            break
                        component[y - 1] = comp_cnt
                if not can:
                    break
                fixed.add(comp_cnt)
        self.result = "YES" if can else "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask771ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
