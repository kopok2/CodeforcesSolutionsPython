class CodeforcesTask217ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.drifts = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.drifts.append([int(y) for y in input().split(" ")])

    def process_task(self):
        x_edges = {}
        y_edges = {}
        for x in range(self.n):
            drift = self.drifts[x]
            if drift[0] in x_edges:
                x_edges[drift[0]].append(x + 1)
            else:
                x_edges[drift[0]] = [x + 1]
            if drift[1] in y_edges:
                y_edges[drift[1]].append(x + 1)
            else:
                y_edges[drift[1]] = [x + 1]
        graph = [[] for x in range(self.n)]
        for x in range(self.n):
            for conn in x_edges[self.drifts[x][0]]:
                if x + 1 != conn:
                    graph[x].append(conn)
            for conn in y_edges[self.drifts[x][1]]:
                if x + 1 != conn:
                    graph[x].append(conn)
        comp_cnt = 0
        component = [0] * self.n
        for x in range(self.n):
            if not component[x]:
                comp_cnt += 1
                to_visit = graph[x][::]
                while to_visit:
                    visiting = to_visit.pop(-1)
                    if not component[visiting - 1]:
                        component[visiting - 1] = comp_cnt
                        to_visit += graph[visiting - 1]
        self.result = str(comp_cnt - 1)



    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask217ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
