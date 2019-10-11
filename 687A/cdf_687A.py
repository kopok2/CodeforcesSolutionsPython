from collections import deque


class CodeforcesTask687ASolution:
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
        for edge in self.edges:
            graph[edge[0] - 1].append(edge[1])
            graph[edge[1] - 1].append(edge[0])
        partite1 = set()
        partite2 = set()
        visited = [False] * self.n_m[0]
        for x in range(self.n_m[0]):
            if not visited[x] and graph[x]:
                to_visit = deque([(x + 1, True)])
                can = True
                while to_visit:
                    visiting = to_visit.popleft()
                    visited[visiting[0] - 1] = True
                    #print(visiting)
                    if visiting[1] and visiting[0] in partite2:
                        can = False
                        break
                    elif not visiting[1] and visiting[0] in partite1:
                        can = False
                        break
                    else:

                        if visiting[1]:
                            if visiting[0] not in partite1:
                                partite1.add(visiting[0])
                                to_visit.extend([(x, not visiting[1]) for x in graph[visiting[0] - 1]])
                        else:
                            if visiting[0] not in partite2:
                                partite2.add(visiting[0])
                                to_visit.extend([(x, not visiting[1]) for x in graph[visiting[0] - 1]])
        #print(partite1, partite2)
        for edge in self.edges:
            if edge[0] in partite1 and edge[1] in partite1:
                can = False
            elif edge[0] in partite2 and edge[1] in partite2:
                can = False
        if can:
            self.result = "{0}\n{1}\n{2}\n{3}".format(len(partite1), " ".join([str(x) for x in list(partite1)]),
                                                      len(partite2), " ".join([str(x) for x in list(partite2)]))
        else:
            self.result = "-1"


    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask687ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
