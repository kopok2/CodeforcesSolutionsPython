class CodeforcesTask755CSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.distant = []

    def read_input(self):
        self.n = int(input())
        self.distant = [int(x) for x in input().split(" ")]

    def process_task(self):
        graph = [[] for x in range(self.n)]
        for x in range(self.n):
            graph[x].append(self.distant[x])
            graph[self.distant[x] - 1].append(x + 1)
        comp = 0
        component = [0] * self.n
        for x in range(self.n):
            if not component[x]:
                comp += 1
                to_visit = [x + 1]
                while to_visit:
                    visiting = to_visit.pop(-1)
                    if not component[visiting - 1]:
                        component[visiting - 1] = comp
                        to_visit += graph[visiting - 1]
        self.result = str(comp)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask755CSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
