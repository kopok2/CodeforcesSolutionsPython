class CodeforcesTask601ASolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.railways = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[1]):
            self.railways.append([int(y) for y in input().split(" ")])

    def process_task(self):
        training = True
        for railway in self.railways:
            if railway == [self.n_m[0], 1] or railway == [1, self.n_m[0]]:
                training = False
                break
        visits = {}
        to_visit = [(1, 0)]
        if training:
            graph = [[] for x in range(self.n_m[0])]
            for railway in self.railways:
                graph[railway[0] - 1].append(railway[1])
                graph[railway[1] - 1].append(railway[0])
        else:
            graph = [[] for x in range(self.n_m[0])]
            for railway in self.railways:
                graph[railway[0] - 1].append(railway[1])
                graph[railway[1] - 1].append(railway[0])
            for x in range(self.n_m[0]):
                graph[x] = list(set([y for y in range(1, self.n_m[0] + 1)]).difference(set(graph[x])))
        while to_visit:
            visiting = to_visit.pop(-1)
            if visiting[0] in visits:
                if visiting[1] < visits[visiting[0]]:
                    visits[visiting[0]] = visiting[1]
                    for adj in graph[visiting[0] - 1]:
                        to_visit.append((adj, visiting[1] + 1))
            else:
                visits[visiting[0]] = visiting[1]
                for adj in graph[visiting[0] - 1]:
                    to_visit.append((adj, visiting[1] + 1))
        if self.n_m[0] in visits:
            self.result = str(visits[self.n_m[0]])
        else:
            self.result = "-1"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask601ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
